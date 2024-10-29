from langchain.document_loaders import DirectoryLoader
import os
from src.exception import CustomeExceptionClass
from src.loggers import logging
import sys
try:
    directory = r'C:\Users\Reyan Alam\Desktop\New folder\yippee'
    logging.info('loading the document')
    def load_docs(directory, file_type="txt"):
        loader = DirectoryLoader(directory, glob=f"*.{file_type}")
        documents = loader.load()
        logging.info('loading successfull')
        return documents

    documents = load_docs(directory, file_type="txt")
except Exception as e:
<<<<<<< HEAD
    raise CustomeExceptionClass(e,sys)
=======
            raise CustomeExceptionClass(e,sys)
>>>>>>> 707750bd44022204c9b456671eb1e98c236be02b
