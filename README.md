![Screenshot (253)](https://github.com/user-attachments/assets/e685176e-084a-4728-8eed-9d5e1d198480)

Project Description: Retrieval-Augmented Generation (RAG) Chatbot
Overview:

Development of a RAG chatbot using Langchain, Pinecone, and Streamlit.
Utilizes advanced natural language processing for accurate and contextually relevant responses.
Key Components:

User Interface with Streamlit:

Interactive web application for user queries and real-time responses.
Intuitive design enhances user experience.
Data Ingestion:

Implemented data_ingestion.py to load documents from a specified directory.
Uses Langchain's DirectoryLoader for reading text files and logging loading status.
Preprocessing of Documents:

preprocessing.py splits documents into manageable chunks using Langchain’s RecursiveCharacterTextSplitter.
Converts text chunks into numerical embeddings with the SentenceTransformer model for semantic matching.
Embedding Storage with Pinecone:

Pinecone serves as a vector database for storing generated embeddings.
Facilitates fast retrieval of relevant information based on user queries.
Conversation Management:

Maintains conversation context using Streamlit's session state.
Uses Langchain’s ConversationChain to manage dialogue history and memory.
Query Refinement and Contextual Matching:

Query Refinement: query_refiner function utilizes OpenAI's GPT-3.5 model to enhance query relevance.
Contextual Matching: find_match function fetches relevant text segments from Pinecone based on refined user input.
Robust Error Handling:

Custom exception handling logs errors during data loading, processing, and querying for improved reliability.
Conclusion:

This RAG chatbot combines NLP techniques and data management to create an intelligent conversational agent.
Integrates Langchain for conversation management, Pinecone for vector storage, and Streamlit for the user interface, showcasing the potential of advanced chatbot development.


