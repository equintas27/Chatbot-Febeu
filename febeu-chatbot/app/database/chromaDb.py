import chromadb

def get_chroma_client():
    client = chromadb.HttpClient(host='chromadb', port=8000)
    return (client)

def get_knowledge_collections():
    client = get_chroma_client()

    collection = client.get_or_create_collection(name="febeu_knowledge")
    return (collection)