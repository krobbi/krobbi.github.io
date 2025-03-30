import os

from . import output
from . import styles
from . import templates

from .templates import Template

_template: Template | None = None
"""The base template for all pages."""

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
    
    style = "home" if path == "index.html" else "page"
    
    template = (
        _get_template()
        .append("url", path.removesuffix("index.html"))
        .append("styles", styles.get_html(style))
        .replace("content", content)
    )
    
    output.write(template.render(), path)


def _get_template():
    """Return the base template for all pages."""
    
    global _template
    
    if _template is None:
        _template = (
            templates.get("base.html")
            .prepend("title", "Krobbizoid")
            .append("url", "https://krobbi.github.io/")
            .append("styles", styles.get_html("main"))
        )
    
    return _template
