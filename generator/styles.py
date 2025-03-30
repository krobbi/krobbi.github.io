import sass

from . import output
from . import templates

_compiled_styles: set[str] = set()
"""The set of style names that have been compiled."""

def get_html(name: str):
    """Return a style's HTML code by its name and output its CSS if
    necessary.
    """
    
    path = f"css/{name}.css"
    
    if name not in _compiled_styles:
        _compiled_styles.add(name)
        filename = f"styles/{name}.scss"
        text = sass.compile(filename=filename, output_style="compressed")
        output.write(text, path)
    
    return templates.get("style.html").replace("path", path).render()
