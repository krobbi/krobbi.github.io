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
    fields: dict[str, str] = {}
    content = ""
    
    with open("pages/" + path) as file:
        for line in file:
            line = line.rstrip()
            
            if line == "---":
                is_parsing_fields = not is_parsing_fields
            if is_parsing_fields:
                pair = line.split(":", 1)
                
                if len(pair) == 2:
                    key = pair[0].strip()
                    value = pair[1].strip()
                    fields[key] = value
            else:
                content += line + "\n"
    
    style = "home" if path == "index.html" else "page"
    
    template = (
        _get_template()
        .append("url", path.removesuffix("index.html"))
        .append("styles", styles.get_html(style))
        .replace("content", content)
    )
    
    title = fields.get("title")
    
    if title is not None:
        template = template.prepend("title", " | ").prepend("title", title)
    
    description = fields.get("description")
    
    if description is not None:
        template = template.replace("description", description)
    
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
