import re

_TAG_PATTERN = re.compile("{\\s*(\\w+)\\s*}")
"""A pattern matching template tags and capturing their names."""

class _Template:
    """A text template with tags that can be replaced or appended to."""
    
    def __init__(self, source: str):
        """Initialize the template from its source text."""
        
        # Normalize tags by removing their whitespace.
        self._source = _TAG_PATTERN.sub("{\\1}", source)
        """The template's internal source text."""
    
    
    def render(self):
        """Return the template as text with any undefined tags
        removed.
        """
        
        return _TAG_PATTERN.sub("", self._source)


def test():
    """Test the template system."""
    
    def normalize(source: str):
        """Return the normalized form of template source text."""
        
        return _Template(source)._source # type: ignore
    
    # Normalized template text has no surrounding whitespace in tags.
    text = normalize("[{no_spaces}, { spaces }, {\t\r\nmixed_spaces}]")
    assert text == "[{no_spaces}, {spaces}, {mixed_spaces}]"
    
    # Numeric and non-ASCII names are valid.
    text = normalize("[{ 1 }, { café }]")
    assert text == "[{1}, {café}]"
    
    # Empty or non-alphanumeric names are invalid.
    text = normalize('[{ }, { separating space }, { / }, { "format":"JSON" }]')
    assert text == '[{ }, { separating space }, { / }, { "format":"JSON" }]'
    
    # Undefined tags are removed from templates when rendered.
    template = _Template("Hello, {undefined}!")
    assert template.render() == "Hello, !"
    
    # Templates are not mutated after rendering.
    assert template._source == "Hello, {undefined}!" # type: ignore
    
    print("Template tests passed!")
