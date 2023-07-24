from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

metadata_field_info = [
    AttributeInfo(
        name="Heading",
        description="The Heading of topic the chunk is from",
        type="string",
    ),
    AttributeInfo(
        name="Subheading",
        description="The Subheading of topic the chunk is from",
        type="string",
    ),
    AttributeInfo(
        name="Question",
        description="The Question that might be asked",
        type="string",
    ),    
]

def retriver(db, llm, document_description="About PAN card", meta_field_info=metadata_field_info):
    retriver= SelfQueryRetriever.from_llm(
        llm,
        db,
        document_description,
        metadata_field_info,
    )
    return retriver

def doc_query_retriver(retriver, query):
    docs = retriver.get_relevant_documents(query)
    return docs





def doc_query_similarity(db,query,top_k=3):
    docs= db.similarity_search(query,k=top_k)
    return docs

def doc_query_vector_similarity(db,query, embeddings,top_k=3):
    e_vector= embeddings.embed_query(query)
    docs= db.similarity_search_by_vector(e_vector,k=top_k)
    return docs

def doc_query_MMR(db,query,top_k=3):
    docs= db.max_marginal_relevance_search(query,k=top_k)
    return docs

