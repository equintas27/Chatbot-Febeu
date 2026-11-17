from app.database.chromaDb import get_knowledge_collections
from app.rag.gen_embeddings import generate_query_embeddings

def retriever_knowledge(question: query, n_results: 5):

    collection = get_knowledge_collections()
    query_embedding = generate_query_embeddings(question)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    return results
