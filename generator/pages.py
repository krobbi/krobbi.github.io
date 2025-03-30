import os

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
    
    print(f"Generate '{path}'.")
