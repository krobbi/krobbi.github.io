from . import license

from ..templates import Template

def render_content(content: str, path: str):
    """Render the content of a page by its path."""
    
    renderer = _get_renderer(path)
    
    if renderer is None:
        return content
    
    return renderer(Template(content)).render()


def _get_renderer(path: str):
    """Return the content renderer function for a path."""
    
    if path == "license/index.html":
        return license.render_license_page
    else:
        return None
