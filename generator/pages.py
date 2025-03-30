import os

from . import output
from . import renderer
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
            elif is_parsing_fields:
                pair = line.split(":", 1)
                
                if len(pair) == 2:
                    key = pair[0].strip()
                    value = pair[1].strip()
                    fields[key] = value
            else:
                content += line + "\n"
    
    content = renderer.render_content(content, path)
    style = "home" if path == "index.html" else "page"
    
    template = (
        _get_template()
        .append("url", path.removesuffix("index.html"))
        .append("styles", styles.get_html(style))
        .replace("content", content)
    )
    
    template = _apply_title(fields, template)
    template = _apply_description(fields, template)
    template = _apply_robots(fields, template)
    output.write(template.render(), path)


def _apply_title(fields: dict[str, str], template: Template):
    """Apply a page title from fields to a template."""
    
    title = fields.get("title")
    
    if title is None:
        return template
    
    return template.prepend("title", " | ").prepend("title", title)


def _apply_description(fields: dict[str, str], template: Template):
    """Apply a page description from fields to a template."""
    
    description = fields.get("description")
    
    if description is None:
        return template
    
    return template.replace("description", description)


def _apply_robots(fields: dict[str, str], template: Template):
    """Apply a robots directive from fields to a template."""
    
    robots = fields.get("robots")
    
    if robots is None:
        return template
    
    robots = templates.get("robots.html").replace("directive", robots).render()
    return template.replace("robots", robots)


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
