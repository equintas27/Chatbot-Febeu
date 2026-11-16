from sentence_transformers import Sentence_Transformers

class EmbeddingModel:
    def __init__(self):
        self.model = Sentence_Transformers("paraphrase-multilingual-MiniLM-L12-v2")