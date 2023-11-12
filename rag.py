# ========================= RETRIEVAL AUGMENTED GENERATION =========================
import chromadb
import openai
import os

from chromadb.utils import embedding_functions

def get_chroma_collection (collection_name):
    chroma_client = chromadb.PersistentClient(path=".")

    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                    api_key=os.getenv("OPENAI_API_KEY"),
                    api_base=os.getenv("OPENAI_API_BASE"),
                    model_name="text-embedding-ada-002"
                )
    
    collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=openai_ef)
    return collection


def get_chroma_collection(collection_name):
    chroma_client = chromadb.PersistentClient(path=".")

    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                    api_key=os.getenv("OPENAI_API_KEY"),
                    api_base=os.getenv("OPENAI_API_BASE"),
                    model_name="text-embedding-ada-002"
                )

    collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=openai_ef)
    return collection

def add_dataset_to_collection(dataset, collection):
    documents = []
    metadatas = []
    ids = []

    for i, row in enumerate(text):
        # grabs attributes from df
        source = dataset['source']
        text = dataset['text']

        # specific attributes being embedded
        embeddable_string = f"{source}{text}"
        documents.append(embeddable_string)

        # stores as metadata
        metadatas.append(dataset)

        # index as id
        ids.append(str(i))

    # updates collection
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )