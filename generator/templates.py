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
    
    
    def replace(self, tag: str, text: str):
        """Return a copy with a tag replaced with text."""
        
        return _Template(self._source.replace("{" + tag + "}", text))
    
    
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
    
    # Tags can be replaced.
    template = _Template("I like {fruit}.")
    assert template.replace("fruit", "apples").render() == "I like apples."
    
    # Replacing tags creates a copy instead of mutating the template.
    assert template.render() == "I like ."
    
    # The original template can be reused because of this.
    assert template.replace("fruit", "bananas").render() == "I like bananas."
    
    # All tags with the same name are replaced at once.
    template = _Template("{adjective} templates are {adjective}")
    text = template.replace("adjective", "reusable").render()
    assert text == "reusable templates are reusable"
    
    # JSON objects are not removed when rendered.
    template = _Template("{value:{value}}{}")
    assert template.replace("value", "123").render() == "{value:123}{}"
    
    print("Template tests passed!")
