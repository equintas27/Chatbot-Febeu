import chromadb
from app.rag.gen_embeddings import generate_embeddings


def get_chroma_client():
    client = chromadb.HttpClient(host='chromadb', port=8000)
    return (client)

def get_knowledge_collections():
    client = get_chroma_client()
    collection = client.get_or_create_collection(
        name="febeu_knowledge", 
        metadata={"hnsw:space": "cosine"}
    )

    new_chunks = generate_embeddings()
    print(len(new_chunks))
    ids = []
    texts = []
    embeddings = []
    metadatas = []

    for chunk in new_chunks:
        ids.append(chunk["id"])
        texts.append(chunk["text"])
        embeddings.append(chunk["embeddings"])
        metadatas.append(chunk["metadata"])

    collection.upsert(
        ids=ids,
        documents=texts, 
        embeddings=embeddings,
        metadatas=metadatas
    )

    return (collection)

