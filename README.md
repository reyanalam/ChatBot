![Screenshot (253)](https://github.com/user-attachments/assets/e685176e-084a-4728-8eed-9d5e1d198480)

# Retrieval-Augmented Generation (RAG) Chatbot

## Overview

This project involves the development of a **Retrieval-Augmented Generation (RAG) Chatbot** using **Langchain**, **Pinecone**, and **Streamlit**. The chatbot utilizes advanced natural language processing (NLP) techniques to generate accurate and contextually relevant responses by retrieving information from a large corpus of documents.

## Key Components

### 1. **User Interface with Streamlit**
- Interactive web application for user queries and real-time responses.
- The interface is intuitive, enhancing the user experience.

### 2. **Preprocessing of Documents**
- Splits documents into manageable chunks using .
- Converts text chunks into numerical embeddings using **SentenceTransformer** for semantic matching.

### 4. **Embedding Storage with Pinecone**
- **Pinecone** is used as a vector database for storing the generated embeddings.
- Facilitates fast retrieval of relevant information based on user queries.

### 5. **Conversation Management**
- Maintains conversation context using **Streamlit's session state**.
- Uses **Langchain’s ConversationChain** to manage dialogue history and memory.

### 6. **Query Refinement and Contextual Matching**
- **Query Refinement:** The `query_refiner` function utilizes **OpenAI's GPT-3.5** model to enhance the relevance of the user’s query.
- **Contextual Matching:** The `find_match` function fetches relevant text segments from **Pinecone** based on the refined user input.

### 7. **Robust Error Handling**
- Custom exception handling ensures any errors during data loading, processing, and querying are logged, improving system reliability.

## Conclusion

This **RAG Chatbot** combines advanced **NLP techniques** and efficient **data management** to create an intelligent conversational agent. It integrates **Langchain** for conversation management, **Pinecone** for vector storage, and **Streamlit** for the user interface, showcasing the potential of advanced chatbot development.

## Technologies Used
- **Langchain**: For conversation management and document processing.
- **Pinecone**: Vector database for storing and retrieving document embeddings.
- **Streamlit**: For creating the web-based user interface.
- **OpenAI GPT-3.5**: For query refinement and enhancing user input relevance.
- **SentenceTransformer**: For generating document embeddings.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/rag-chatbot.git

2. Install all the dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the main program:
   ```bash
   python run main.py

4. Run the app.py file:
   ```bash
   streamlit run app.py

Ask questions from the ChatBot

## Contact

1. **Linkedin:** https://www.linkedin.com/in/reyanalam/
2. **Gmail:** reyanalam115@gmail.com






