import os

from . import output

def generate_pages():
    """Generate the site's pages."""
    
    _generate_pages_recursive("")


def _generate_pages_recursive(dir: str):
    """Recursively generate the site's pages in a directory."""
    
    for entry in os.scandir("pages/" + dir):
        path = dir + entry.name
        
        if entry.is_dir():
            _generate_pages_recursive(path + "/")
        else:
            _generate_page(path)


def _generate_page(path: str):
    """Generate a page by its path."""
    
    is_parsing_fields = False
    content = ""
    
    with open("pages/" + path) as file:
        for line in file:
            line = line.rstrip()
            
            if line == "---":
                is_parsing_fields = not is_parsing_fields
            elif not is_parsing_fields:
                content += line + "\n"
    
    output.write(content, path)
