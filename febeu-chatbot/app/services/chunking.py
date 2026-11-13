from pathlib import Path
from app.services.tokenizer import TextTokenizer

def read_document():
    document = Path("/app/knowledge_base/FEBEU_ENTERPRISE.md")
    try:
        content = document.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError("ERROR! ao ler o arquivo")
    return content

def count_tokens(section: str):
    text_tokenizer = TextTokenizer()

    tokens = text_tokenizer.Tokenizer.tokenize(section["content"])
    return len(tokens)

def create_chunk(sections: list, chunk_size: int, overlap: int):

    Chunks = []
    Chunks_title = None
    Chunks_content

    if chunk_size <= 0 or overlap <= 0:
        raise RuntimeError("O chunk_size or overlap não podem iguais ou menores que 0")
    
    for section in sections:

