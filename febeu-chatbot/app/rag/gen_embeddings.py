from app.rag.embedder import EmbeddingModel
from app.services.markdown_parser import markdown_parsing
from app.services.chunking import create_chunk

model = EmbeddingModel()

def generate_embeddings() :

    content = markdown_parsing()
    chunks = create_chunk(content, 150, 45)
   
    for chunk in chunks:
        embeddings = model.embedding_documents(chunk["text"])
        chunk["embeddings"] = embeddings
    return chunks


def generate_query_embeddings(query) -> list[float]: 

    query_embedding = model.embedding_query(query)
    return query_embedding


