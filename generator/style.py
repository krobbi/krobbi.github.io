import sass

import output
import template

_compiled_styles: set[str] = set()
"""The set of style names that have been compiled."""

def get_html(name: str):
    """Return a style's HTML code by its name and output its CSS if
    necessary.
    """
    
    path = f"css/{name}.css"
    
    if name not in _compiled_styles:
        filename = f"styles/{name}.scss"
        text = sass.compile(filename=filename, output_style="compressed")
        output.write(text, path)
    
    return template.get("style.html").replace("path", path).render()
