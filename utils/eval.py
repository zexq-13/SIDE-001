import pandas as pd
from langchain.evaluation.qa import QAEvalChain
from embeddings import *
from loader import *
from QA import *
from retrival import *
from splitter import *
from vectorstore import *


def create_df(filepath):
    df=pd.read_excel(filepath)
    return df

def get_eval(llm,examples, preds):
    eval_chain = QAEvalChain.from_llm(llm)
    grades= eval_chain.evaluate(examples, preds)
    count=0
    for i in grades:
        if(i['results']=='CORRECT'):
            count+=1
    return count/len(grades)

if __name__ == '__main__':
    df=create_df('.\Dataset\SampleQuestions.xlsx')
    info=load_from_txt("./Dataset/Data.txt")
    md_split=markdown_split(info[0].page_content)
    embeddings=openai_embeddings()
    db=chroma_db(md_split,embeddings)
    lm=llm()
    qa=qa_retrival_chain(db, lm)
    examples=[]
    Q=[x for x in df['Question']]
    A=[x for x in df['Ideal Answer']]
    for i in range(len(Q)):
        examples.append({'query':Q[i], 'answer': A[i]})
    chat_history=[]
    predictions=[]
    for x in Q:
        y=qa({"question": x,"chat_history": chat_history})["answer"]
        predictions.append(y)
    preds=[]
    for x,y,z in zip(Q,predictions,A):
        preds.append({'query':x,'answer':z, 'result':y})
    print("Accuracy: " )
    print(get_eval(lm,examples, preds))
