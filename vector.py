from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# read csv
df = pd.read_csv("products-100.csv")

# embedding model 
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# chroma db location where we want to store our vector database
db_location = "./chroma_langchain_db"
# checking db location already exists if already exists no need to 
add_documents = not os.path.exists(db_location) #If the file exists (True), not makes it False.
                                     #If the file does not exist (False), not makes it True.
# creating documents
if add_documents:
    documents  = []
    ids = []

    for i, row in df.iterrows():  #to read csv row by row
        document = Document(
            page_content= row["Name"] + " " + str(row["Description"]),
            metadata = {"Price": row["Price"], "Brand": row["Brand"]},
            id = str(i)
        )
        print(document)
        ids.append(str(i))
        documents.append(document)

# Creating vector store
vector_store = Chroma(
    # collection_name = "products prize",
    # chromadb.errors.InvalidArgumentError: Validation error: name: Expected a name 
    # containing 3-512 characters from [a-zA-Z0-9._-], 
    # starting and ending with a character in [a-zA-Z0-9]. Got: products prize
    collection_name = "name_price",
    persist_directory = db_location, # no need to regenerating this chroma database
    embedding_function = embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids = ids)

# connecting LLM & Vectore store
# as_retriever used to lookup documents
retriever = vector_store.as_retriever(
    search_kwargs = {"k": 5} # to look up five relavant products. k = 5 or 1 or 10
)