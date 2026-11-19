from app.services.chunking import read_document

def save_sections(section: list, title: str, content: list):
    if title:
        section.append({"title": title,
        "content": "\n".join(content)}
        )

def markdown_parsing():
    content = read_document()
    lines = content.splitlines()

    sections = []
    current_title = None
    current_content = []
    current_parent = []
    for line in lines:
        if line.startswith("## ") and not line.startswith("### "):
            save_sections(sections, current_title, current_content)
            current_title = line
            current_parent = line
            current_content = []
        elif line.startswith("### "):
            save_sections(sections, current_title, current_content)
            current_title = f"{current_parent} > {line}"
            current_content = []
        else:
            current_content.append(line)
    
    save_sections(sections, current_title, current_content)
    
    return sections
