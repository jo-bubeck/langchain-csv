import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.llms import AzureOpenAI
from Secrets.apikey import API_KEY

def initialize_chatbot(data_file_path):
    os.environ["OPENAI_API_TYPE"] = "azure"
    os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
    os.environ["OPENAI_API_BASE"] = "https://mhpai.openai.azure.com/"
    os.environ["OPENAI_API_KEY"] = API_KEY

    loader = CSVLoader(file_path=data_file_path, encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()

    embeddings = OpenAIEmbeddings(chunk_size=10)
    vectorstore = FAISS.from_documents(data, embeddings)

    chain = ConversationalRetrievalChain.from_llm(
        llm=AzureOpenAI(model_name="gpt-4-32k", engine="gpt-4-32k"),
        retriever=vectorstore.as_retriever()
    )

    return chain

def conversational_chat(chain, query, history=[]):
    result = chain({"question": query, "chat_history": history})
    history.append((query, result["answer"]))
    return result["answer"]