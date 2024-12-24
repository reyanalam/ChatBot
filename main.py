import os
import pinecone
import openai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from src.exception import CustomeExceptionClass
import sys
from langchain.embeddings import SentenceTransformerEmbeddings

load_dotenv(dotenv_path=r"C:\Users\Reyan\Desktop\Projects\chatbot\ChatBot\api.env")
# Setting OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initializing Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = pinecone.Pinecone(api_key=pinecone_api_key)
index = pc.Index('chatbot')


llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, max_length=1000):
    """Splits text into chunks of a specified maximum length."""
    words = text.split()
    chunks = []
    chunk = []

    for word in words:
        if len(" ".join(chunk + [word])) > max_length:
            chunks.append(" ".join(chunk))
            chunk = [word]
        else:
            chunk.append(word)

    if chunk:
        chunks.append(" ".join(chunk))

    return chunks

def embed_text(text_chunks):
    """Generates embeddings for a list of text chunks using TF-IDF."""
    model_name = "all-MiniLM-L6-v2"
    
    # Wrap the model with SentenceTransformerEmbeddings
    embeddings = SentenceTransformerEmbeddings(model_name=model_name)
    
    # Generate embeddings for the input text chunks
    embeddings_list = embeddings.embed_documents(text_chunks)
    
    return embeddings_list


def store_embeddings_in_pinecone(embeddings, text_chunks):
    """Stores embeddings and their associated text chunks in Pinecone."""
    for i, (embedding, chunk) in enumerate(zip(embeddings, text_chunks)):
        metadata = {"text": chunk}
        index.upsert([(f"doc-{i}", embedding, metadata)])

def find_match(input):
    """Finds relevant text matches from Pinecone based on input."""
    input_em = embed_text([input])[0]  # Generate embedding for input
    result = index.query(input_em, top_k=2, includeMetadata=True)
    return result['matches'][0]['metadata']['text'] + "\n" + result['matches'][1]['metadata']['text']

def query_refiner(conversation, query):
    """Refines a user query based on the conversation context."""
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def get_conversation_string():
    """Constructs the conversation history as a string."""
    conversation_string = ""
    for i in range(len(st.session_state['responses']) - 1):
        conversation_string += "Human: " + st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + st.session_state['responses'][i + 1] + "\n"
    return conversation_string



if __name__ == "__main__":
    pdf_path = "pdf.pdf"

    # Step 1: Extract text from the PDF
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Chunk the text
    print("Chunking text...")
    text_chunks = chunk_text(text)

    # Step 3: Generate embeddings for the text chunks
    print("Generating embeddings...")
    embeddings = embed_text(text_chunks)

    # Step 4: Store the embeddings in Pinecone
    print("Storing embeddings in Pinecone...")
    store_embeddings_in_pinecone(embeddings, text_chunks)

    print("Data ingestion complete!")
