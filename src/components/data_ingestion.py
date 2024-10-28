from langchain.document_loaders import DirectoryLoader
import os

directory = r'C:\Users\Reyan Alam\Desktop\New folder\yippee'

def load_docs(directory, file_type="txt"):
    loader = DirectoryLoader(directory, glob=f"*.{file_type}")
    documents = loader.load()
    return documents

documents = load_docs(directory, file_type="txt")
