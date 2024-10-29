Project Title: RAG Chatbot Application

Project Description:

This project features the development of a Retrieval-Augmented Generation (RAG) chatbot, utilizing Langchain, Pinecone, and Streamlit. The application leverages advanced natural language processing techniques to deliver accurate and contextually relevant responses to user queries.

Key Components:
User Interface with Streamlit:

Built an interactive web application using Streamlit, which allows users to input queries and receive real-time responses. The intuitive interface facilitates smooth interaction, enhancing the user experience.
Data Ingestion:

Implemented a data_ingestion.py script to load documents from a specified directory. Using Langchain's DirectoryLoader, the application reads text files and prepares them for further processing, logging the status of the loading process.
Preprocessing of Documents:

The preprocessing.py script is responsible for splitting the loaded documents into manageable chunks using Langchain’s RecursiveCharacterTextSplitter. This segmentation ensures that the documents can be effectively embedded and stored in a vector database.
Additionally, the script converts text chunks into numerical embeddings using the SentenceTransformer model, allowing for efficient semantic matching and retrieval.
Embedding Storage with Pinecone:

The application employs Pinecone as a vector database, where the generated embeddings are stored. This setup enables fast and efficient retrieval of relevant information based on user queries.
Conversation Management:

The chatbot maintains the context of conversations by using Streamlit's session state, allowing users to have continuous dialogues without losing previous interactions.
The conversation state is managed through the ConversationChain in Langchain, incorporating memory to recall the last few exchanges.
Query Refinement and Contextual Matching:

A two-step approach for handling user queries is implemented:
Query Refinement: The query_refiner function uses OpenAI's GPT-3.5 model to formulate more relevant queries based on the conversation history, improving the chances of retrieving accurate information.
Contextual Matching: The find_match function queries Pinecone to fetch the most relevant text segments corresponding to the refined user input, ensuring the chatbot can provide informed answers.
Robust Error Handling:

Custom exception handling is implemented throughout the application, ensuring that errors during data loading, processing, and querying are logged appropriately, enhancing the application's reliability.
Conclusion:
This RAG chatbot application effectively combines cutting-edge NLP techniques and robust data management to create an intelligent conversational agent. By leveraging Langchain for conversation management, Pinecone for vector storage, and Streamlit for the user interface, this project showcases the potential of integrating various technologies to build an advanced chatbot capable of delivering valuable insights and enhancing user interaction.
![Screenshot (253)](https://github.com/user-attachments/assets/386c5d77-5477-42c8-ad23-b947d45be6f5)

