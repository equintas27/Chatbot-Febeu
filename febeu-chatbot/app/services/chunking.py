from pathlib import Path
from app.services.tokenizer import TextTokenizer

def read_document():
    document = Path("/app/knowledge_base/FEBEU_ENTERPRISE.md")
    try:
        content = document.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError("ERROR! ao ler o arquivo")
    return content

# def create_chunk(sections: list, chunk_size: int, overlap: int):

#     t_chunks = []
#     chunks = []
#     token_content = []
#     text_tokenizer = TextTokenizer()

#     if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
#         raise ValueError("Parâmetros de chunking inválidos.")
    
#     for section in sections:
#         token_content = text_tokenizer.Tokenizer.encode(section["content"], add_special_tokens=False, truncation=False)
#         start = 0
#         while start < len(token_content):
#             end = start + chunk_size
#             chunk_token = token_content[start:end]
#             chunk = {
#                 "title": section["title"],
#                 "chunk_token": chunk_token,
#                 "length_token": len(chunk_token)
#             }
#             start += chunk_size - overlap
#             t_chunks.append(chunk)

#     # for t_chunk in t_chunks:
#         chunk_text = text_tokenizer.Tokenizer.decode(t_chunk["chunk_token"], skip_special_tokens=True)
#         chunks.append({
#                 "title": t_chunk["title"],
#                 "text": chunk_text,
#                 "length_text": len(chunk_text)
#             }
#         )
#     return chunks

# def create_chunk(sections: list, chunk_size: int, overlap: int):

#     chunks = []
#     text_tokenizer = TextTokenizer()

#     if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
#         raise ValueError("Parâmetros de chunking inválidos.")

#     for section in sections:

#         original_text = section["content"]

#         result = text_tokenizer.Tokenizer(
#             original_text,
#             add_special_tokens=False,
#             return_offsets_mapping=True
#         )

#         token_content = result["input_ids"]
#         offset_mapping = result["offset_mapping"]

#         start = 0

#         while start < len(token_content):

#             end = min(start + chunk_size, len(token_content))

#             start_char = offset_mapping[start][0]
#             end_char = offset_mapping[end - 1][1]

#             chunk_text = original_text[start_char:end_char]

#             chunks.append({
#                 "title": section["title"],
#                 "text": chunk_text,
#                 "length_token": end - start
#             })

#             if end >= len(token_content):
#                 break

#             start += chunk_size - overlap

#     return chunks


def create_chunk(sections: list, chunk_size: int, overlap: int):

    chunks = []
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
        offset_mapping = result["offset_mapping"]

        start = 0

        while start < len(token_content):

            end = min(start + chunk_size, len(token_content))

            start_char = offset_mapping[start][0]
            end_char = offset_mapping[end - 1][1]

            # Ajustar o início para não começar a meio de uma palavra
            if start > 0:
                while start_char > 0 and not original_text[start_char - 1].isspace():
                    start_char -= 1

            # Ajustar o final para não terminar a meio de uma palavra
            if end < len(token_content):
                while end_char > start_char and not original_text[end_char].isspace():
                    end_char -= 1

            chunk_text = original_text[start_char:end_char]

            chunk_length = len(
                text_tokenizer.Tokenizer.encode(
                    chunk_text,
                    add_special_tokens=False
                )
            )

            if chunk_text.strip():
                chunks.append({
                    "title": section["title"],
                    "text": chunk_text.strip(),
                    "length_token": chunk_length
                })

            if end >= len(token_content):
                break

            start += chunk_size - overlap

    return chunks



