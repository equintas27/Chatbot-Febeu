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

    chunks = []
    token_content = []
    text_tokenizer = TextTokenizer()

    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Parâmetros de chunking inválidos.")
    
    for section in sections:
        
        original_text = section["content"]

        result = text_tokenizer.Tokenizer(
        original_text, 
        add_special_tokens=False, 
        return_offsets_mapping=True
        )

        token_content = result["input_ids"]
        mapping_token = result["offset_mapping"]
        start = 0
        size_token = len(token_content)

        while start < size_token:

            end = min (start + chunk_size, size_token)

            if end >= size_token:
                break 
            
            chunk_token = token_content[start:end]

            start_char = mapping_token[start]

            end_char = mapping_token[end - 1]

            chunk_text = original_text[start_char:end_char]
            chunk = {
                "title": section["title"],
                "text": chunk_text,
                "length_token": len(chunk_token)
            }
            start += chunk_size - overlap
            chunks.append(chunk)

    return chunks





