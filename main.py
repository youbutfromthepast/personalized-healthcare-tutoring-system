# original imports
import chunker
import rag

# package imports
import openai
import chromadb
import sqlite3

# Text chunks list
chunks = chunker.text_chunker()
print(chunks.type())

# chroma collection
collection = rag.get_chroma_collection("dataset")
rag.add_df_to_collection(chunks, collection)

# results check
results = rag.get_results("cardio", collection)
for result in results:
    print(results)
