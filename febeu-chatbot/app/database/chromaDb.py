import chromadb
from app.rag.gen_embeddings import generate_embeddings


def get_chroma_client():
    client = chromadb.HttpClient(host='chromadb', port=8000)
    return (client)

def get_knowledge_collections():
    client = get_chroma_client()
    collection = client.get_or_create_collection(name="febeu_knowledge")

    new_chunks = generate_embeddings()

    collection.upsert(
        ids=[new_chunks["id"]],
        text=[new_chunks["text"]],
        embeddings=[new_chunks["embeddings"]], 
        metadata=[new_chunks["metadata"]]
    )
    return (collection)

