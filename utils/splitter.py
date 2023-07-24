from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import MarkdownHeaderTextSplitter

def char_split(data, chunksize=750, chunkoverlap=100):
    text_splitter= CharacterTextSplitter(
        separator="# ",
        chunk_size=chunksize,
        chunk_overlap=chunkoverlap,
        length_function=len
    )
    divided_docs= text_splitter.split_documents(data)
    return divided_docs

default_headers= [
    ("#", "Heading"),
    ("##", "Subheading"),
    ("###", "Question"),
]

def markdown_split(data,headers_split=default_headers):
    markdown_splitter=MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_split
    )
    md_header_splits=markdown_splitter.split_text(data)
    return md_header_splits



