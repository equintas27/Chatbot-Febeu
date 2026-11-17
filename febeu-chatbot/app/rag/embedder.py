from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    def embedding_documents(self, texts: list[str]) -> list[list[float]]: 
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return embeddings.tolist()

    def embedding_query(self, query: str) -> list[float]:
        embedding = self.model.encode(query, normalize_embeddings=True)
        return embedding.tolist()


