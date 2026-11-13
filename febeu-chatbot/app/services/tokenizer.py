from transformers import AutoTokenizer

class TextTokenizer:
    def __init__(self):
        self.Tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")