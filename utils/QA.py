import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain



template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible but be as informative as possible. Always say "Thanks for asking! Feel free to ask anymore Questions" at the end of the answer. 
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],template=template,)

llm_name = "gpt-3.5-turbo"

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

def llm(llm_name=llm_name, temp=0,key=openai.api_key):
    llm = ChatOpenAI(model_name=llm_name, temperature=temp,openai_api_key=key)
    return llm

def qa_chain_from_promt(db, llm, promt=QA_CHAIN_PROMPT):
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        chain_type="stuff",
        retriever=db.as_retriever(),
        chain_type_kwargs={"prompt": promt}
    )
    return qa_chain


def qa_retrival_chain(db, llm):
    qa= ConversationalRetrievalChain.from_llm(
        llm,
        chain_type="stuff",
        retriever=db.as_retriever(),
        return_generated_question=True
    )
    return qa







