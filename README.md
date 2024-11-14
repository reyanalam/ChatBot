![Screenshot (253)](https://github.com/user-attachments/assets/e685176e-084a-4728-8eed-9d5e1d198480)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAG Chatbot Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            text-align: center;
            color: #333;
        }
        .section {
            margin-bottom: 20px;
        }
        .section ul {
            list-style-type: none;
            padding: 0;
        }
        .section ul li {
            margin: 5px 0;
        }
        .key-components ul {
            margin-left: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Retrieval-Augmented Generation (RAG) Chatbot Project</h1>
    
    <div class="section">
        <h2>Overview</h2>
        <p>Development of a RAG chatbot using Langchain, Pinecone, and Streamlit. Utilizes advanced natural language processing for accurate and contextually relevant responses.</p>
    </div>

    <div class="section key-components">
        <h2>Key Components</h2>
        <ul>
            <li><strong>User Interface with Streamlit:</strong>
                <ul>
                    <li>Interactive web application for user queries and real-time responses.</li>
                    <li>Intuitive design enhances user experience.</li>
                </ul>
            </li>
            <li><strong>Data Ingestion:</strong>
                <ul>
                    <li>Implemented <code>data_ingestion.py</code> to load documents from a specified directory.</li>
                    <li>Uses Langchain's DirectoryLoader for reading text files and logging loading status.</li>
                </ul>
            </li>
            <li><strong>Preprocessing of Documents:</strong>
                <ul>
                    <li><code>preprocessing.py</code> splits documents into manageable chunks using Langchain’s RecursiveCharacterTextSplitter.</li>
                    <li>Converts text chunks into numerical embeddings with the SentenceTransformer model for semantic matching.</li>
                </ul>
            </li>
            <li><strong>Embedding Storage with Pinecone:</strong>
                <ul>
                    <li>Pinecone serves as a vector database for storing generated embeddings.</li>
                    <li>Facilitates fast retrieval of relevant information based on user queries.</li>
                </ul>
            </li>
            <li><strong>Conversation Management:</strong>
                <ul>
                    <li>Maintains conversation context using Streamlit's session state.</li>
                    <li>Uses Langchain’s ConversationChain to manage dialogue history and memory.</li>
                </ul>
            </li>
            <li><strong>Query Refinement and Contextual Matching:</strong>
                <ul>
                    <li><strong>Query Refinement:</strong> <code>query_refiner</code> function utilizes OpenAI's GPT-3.5 model to enhance query relevance.</li>
                    <li><strong>Contextual Matching:</strong> <code>find_match</code> function fetches relevant text segments from Pinecone based on refined user input.</li>
                </ul>
            </li>
            <li><strong>Robust Error Handling:</strong>
                <ul>
                    <li>Custom exception handling logs errors during data loading, processing, and querying for improved reliability.</li>
                </ul>
            </li>
        </ul>
    </div>

    <div class="section">
        <h2>Conclusion</h2>
        <p>This RAG chatbot combines NLP techniques and data management to create an intelligent conversational agent. It integrates Langchain for conversation management, Pinecone for vector storage, and Streamlit for the user interface, showcasing the potential of advanced chatbot development.</p>
    </div>
</div>

</body>
</html>



