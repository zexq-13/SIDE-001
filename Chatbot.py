from utils.embeddings import *
from utils.loader import *
from utils.QA import *
from utils.retrival import *
from utils.splitter import *
from utils.vectorstore import *

if __name__ == '__main__':
    info=load_from_txt("./Dataset/Data.txt")
    md_split=markdown_split(info[0].page_content)
    embeddings=openai_embeddings()
    db=chroma_db(md_split,embeddings)
    lm=llm()
    qa=qa_retrival_chain(db, lm)
    query=input("Enter Query \nUser:")
    chat_history = []
    while(1):
        if (query=="end" or query==""):
            print("Chatbot: Session Complete!")
            break
        else:
            result=qa({"question": query,"chat_history": chat_history})
            chat_history.extend([(query, result["answer"])])
            print("Chatbot:"+result['answer']+"\n")
            query=input("User: ")