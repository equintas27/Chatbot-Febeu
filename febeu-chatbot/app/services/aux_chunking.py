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

def group_content(units: list[str], chunk_size: int, text_tokenizer):
    
    chunk = []

    current_chunk = []

    current_tokens = 0

    for unit in units:
        
