from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

openai_api_key = ""


loader = DirectoryLoader('./data', glob='**/*.txt')
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
docsearch = FAISS.from_documents(texts, embeddings)

llm = OpenAI(openai_api_key=openai_api_key)
qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())


def handler(**inputs):
    query = inputs["query"]
    response = qa.run(query)
    return {"pred": response}


if __name__ == "__main__":
    query = "What is the meaning of life?"
    handler(query)
