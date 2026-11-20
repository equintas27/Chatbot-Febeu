from app.services.tokenizer import TextTokenizer

def split_content(original_text: str):
    
    splitted_content = []
    paragragh = []
    
    lines = original_text.splitlines()

    for line in lines:
        if line.strip().startswith("- "):
            if paragragh:
                all_paragraph = "\n".join(paragragh)
                splitted_content.append(all_paragraph)
                paragragh.clear()
            splitted_content.append(line)
        elif line.strip():
            paragragh.append(line)
        elif not line.strip():
            if paragragh:
                all_paragraph = "\n".join(paragragh)
                splitted_content.append(all_paragraph)
                paragragh.clear()
    if paragragh:
        all_paragraph = "\n".join(paragragh)
        splitted_content.append(all_paragraph)
        paragragh.clear()    

    return splitted_content

def group_content(units: list[str], chunk_size: int, text_tokenizer: TextTokenizer):
    
    chunk = []

    current_chunk = []

    current_tokens = 0

    for unit in units:
        result = text_tokenizer.Tokenizer(
            unit,
            add_special_tokens=False
        )

        unit_tokens = len(result["input_ids"])
        if current_tokens + unit_tokens <= chunk_size:
            current_chunk.append(unit)
            current_tokens += unit_tokens
        else:
            aux_chunk = "\n".join(current_chunk)
            chunk.append(aux_chunk)
            current_chunk.clear()
            current_tokens = 0
            current_chunk.append(unit)
            current_tokens += unit_tokens
    
    if current_chunk:
        aux_chunk = "\n".join(current_chunk)
        chunk.append(aux_chunk)
    return chunk

