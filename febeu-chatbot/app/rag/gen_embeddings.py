from app.rag.embedder import EmbeddingModel
from app.services.markdown_parser import markdown_parsing
from app.services.chunking import create_chunk

def generate_embeddings() :

    model = EmbeddingModel()
    content = markdown_parsing()
    chunks = create_chunk(content, 100, 30)
   
    embeddings = model.embedding_documents(chunks["content"])
    chunks["embeddings"] = embeddings
    return chunks




