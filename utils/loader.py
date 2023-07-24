from langchain.document_loaders import TextLoader
from langchain.document_loaders.csv_loader import CSVLoader

def load_from_txt(filepath):
    loader=TextLoader(filepath,encoding='utf-8')
    return loader.load()

def load_from_csv(filepath):
    loader= CSVLoader(filepath, encoding='utf-8')
    return loader

