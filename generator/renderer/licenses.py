from ..templates import Template

def render_licenses_page(template: Template):
    """Render the content for the site's licenses page."""
    
    return (
        template
        .append("licenses", "<li>Foo.</li>")
        .append("licenses", "<li>Bar.</li>")
        .append("licenses", "<li>Baz.</li>")
    )
