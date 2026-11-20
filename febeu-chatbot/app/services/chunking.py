from pathlib import Path
from app.services.tokenizer import TextTokenizer
from app.services.aux_chunking import split_content, group_content

def read_document():
    document = Path("/app/knowledge_base/FEBEU_ENTERPRISE.md")
    try:
        content = document.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError("ERROR! ao ler o arquivo")
    return content


def create_chunk(sections: list, chunk_size: int, overlap: int):
    
    text_tokenizer = TextTokenizer()
    
    chunks = []

    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Parâmetros de chunking inválidos.")
    
    id_chunk = 0
    
    for section in sections:
        
        original_text = section["content"]

        splitted_content = split_content(original_text)

        grouped_content = group_content(splitted_content, chunk_size, text_tokenizer)

        for content in grouped_content:
            tokens = text_tokenizer.Tokenizer(
                content,
                add_special_tokens=False
            )
            chunk = {
                "id" : str(id_chunk),
                 "text": f"{section['title']}\n\n{section['content']}",
                 "metadata":
                 {
                     "title": section["title"],
                     "source": "FEBEU_ENTERPRISE.md",
                    "length_token": len(tokens["input_ids"]) 
                 }
             }
            chunks.append(chunk)
            id_chunk += 1

    return chunks       
        



    



# def create_chunk(sections: list, chunk_size: int, overlap: int):

#     chunks = []
#     token_content = []
#     text_tokenizer = TextTokenizer()

#     if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
#         raise ValueError("Parâmetros de chunking inválidos.")
    
#     id_chunk = 0
#     for section in sections:
        
#         original_text = section["content"]

#         all_lines = split_content(original_text)
#         print (all_lines)

#         result = text_tokenizer.Tokenizer(
#         original_text, 
#         add_special_tokens=False, 
#         return_offsets_mapping=True
#         )

#         token_content = result["input_ids"]
#         mapping_token = result["offset_mapping"]
#         start = 0
#         size_token = len(token_content)
        
#         while start < size_token:

#             end = min(start + chunk_size, size_token)

#             chunk_token = token_content[start:end]
#             #print (len(chunk_token))
#             start_char = mapping_token[start][0]
#             while start_char > 0 and not original_text[start_char].isspace():
#                 start_char -= 1
#             start_char += 1
#             end_char = mapping_token[end - 1][1]
#             while end_char < len(original_text) and not original_text[end_char].isspace():
#                 end_char += 1
#             chunk_text = original_text[start_char:end_char]
#             chunk = {
#                 "id" : str(id_chunk),
#                 "text": f"{section['title']}\n\n{chunk_text}",
#                 "metadata":
#                 {
#                     "title": section["title"],
#                     "source": "FEBEU_ENTERPRISE.md",
#                     "length_token": len(chunk_token) 
#                 }
#             }
#             start += chunk_size - overlap
#             chunks.append(chunk)
#             id_chunk += 1

#     return chunks





