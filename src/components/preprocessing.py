from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.components.data_ingestion import documents
from src.exception import CustomeExceptionClass
from src.loggers import logging
import sys
from langchain.embeddings import SentenceTransformerEmbeddings
import pinecone 
from langchain.vectorstores import Pinecone

try:
    logging.info('splitting the documents into smaller chunks')
    def split_docs(documents,chunk_size=500,chunk_overlap=20):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(documents)
        return docs

    docs = split_docs(documents)
except Exception as e:
            raise CustomeExceptionClass(e,sys)
try:
    logging.info('converting the chunks into numericals')
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
except Exception as e:
            raise CustomeExceptionClass(e,sys)

try:
    logging.info('storing embeddings in Pinecone')
    pinecone.init(
    api_key="6daa34e9-851b-4dbd-b804-74712f92f693" 
    )
    index_name = "chatbot"
    index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
except Exception as e:
            raise CustomeExceptionClass(e,sys)