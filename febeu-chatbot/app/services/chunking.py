from pathlib import Path
from app.services.tokenizer import TextTokenizer

def read_document():
    document = Path("/app/knowledge_base/FEBEU_ENTERPRISE.md")
    try:
        content = document.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError("ERROR! ao ler o arquivo")
    return content

def create_chunk(sections: list, chunk_size: int, overlap: int):

    t_chunks = []
    chunks = []
    token_content = []
    text_tokenizer = TextTokenizer()

    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Parâmetros de chunking inválidos.")
    
    for section in sections:
        token_content = text_tokenizer.Tokenizer.encode(section["content"], add_special_tokens=False, truncation=False)
        start = 0
        while start < len(token_content):
            end = start + chunk_size
            chunk_token = token_content[start:end]
            chunk = {
                "title": section["title"],
                "chunk_token": chunk_token,
                "length_token": len(chunk_token)
            }
            start += chunk_size - overlap
            t_chunks.append(chunk)

    for t_chunk in t_chunks:
        



    return chunks




