import re

from pathlib import Path

_TEMPLATES_DIR = Path("templates")
"""The path for loading templates."""

_TAG_PATTERN = re.compile("{\\s*(\\w+)\\s*}")
"""A pattern matching template tags and capturing their names."""

class Template:
    """A text template with tags that can be replaced or appended to."""
    
    def __init__(self, source: str):
        """Initialize the template from its source text."""
        
        # Normalize tags by removing their whitespace.
        self._source = _TAG_PATTERN.sub("{\\1}", source)
        """The template's internal source text."""
    
    
    def replace(self, tag: str, text: str):
        """Return a copy with a tag replaced by text."""
        
        return Template(self._source.replace("{" + tag + "}", text))
    
    
    def append(self, tag: str, text: str):
        """Return a copy with text appended to a tag."""
        
        return self.replace(tag, text + "{" + tag + "}")
    
    
    def prepend(self, tag: str, text: str):
        """Return a copy with text prepended to a tag."""
        
        return self.replace(tag, "{" + tag + "}" + text)
    
    
    def render(self):
        """Return the template as text with any undefined tags
        removed.
        """
        
        return _TAG_PATTERN.sub("", self._source)


_loaded_templates: dict[str, Template] = {}
"""A map of template names to loaded templates."""

def get(name: str):
    """Return a template from disk by its name."""
    
    if name not in _loaded_templates:
        with open(_TEMPLATES_DIR / name) as file:
            source = file.read()
        
        _loaded_templates[name] = Template(source)
    
    return _loaded_templates[name]
