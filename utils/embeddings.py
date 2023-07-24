import os
import openai
import sys

from langchain.embeddings.openai import OpenAIEmbeddings




from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.environ['OPENAI_API_KEY']

def openai_embeddings(key=openai.api_key):
    return OpenAIEmbeddings(openai_api_key=key)

#Add BERT embeddings

#Add GloVe embeddings
