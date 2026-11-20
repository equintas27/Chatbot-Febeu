from app.database.chromaDb import get_knowledge_collections
from app.rag.gen_embeddings import generate_query_embeddings
import time

def retriever_knowledge(question: query, n_results: int):

    collection = get_knowledge_collections()
    
    start_emb = time.perf_counter()
    query_embedding = generate_query_embeddings(question)
    end_emb = time.perf_counter()

    start_chromaDb = time.perf_counter()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    end_chromaDb = time.perf_counter()

    #print (f"Embeddings: {end_emb - start_emb:.2f}s")
    #print (f"ChromaDB: {end_chromaDb - start_chromaDb:.2f}s")
    
    return results
