from .. import output
from .. import templates

from ..templates import Template

_LICENSES = [
    # 2025.
    ("mit", "2025"),
    
    # 2024.
    ("kgl", "2024"),
    ("mit", "2024"),
    
    # 2023.
    ("mit", "2023-2024"),
    ("kgl", "2023"),
    ("mit", "2023"),
    
    # 2022.
    ("mit", "2022-2023"),
    ("mit", "2022"),
    
    # 2021.
    ("kgl", "2021-2024"),
    ("kgl", "2021-2023"),
    ("mit", "2021-2023"),
    ("kpogdl", "2021-2022"),
    ("kpogdl", "2021"),
    ("mit", "2021"),
    
    # 2020.
    ("mit", "2020"),
]
"""A list of licenses and their years."""

def render_license_page(template: Template):
    """Render the content for the site's license page."""
    
    for (id, year) in _LICENSES:
        _output_text(id, year.replace("-", "/"), year, "Chris Roberts")
    
    return template


def _output_text(id: str, slug: str, year: str, holder: str):
    """Output a license text by its ID, slug, copyright year, and
    copyright holder.
    """
    
    text = (
        templates.get(f"license/texts/{id}.txt")
        .replace("year", year)
        .replace("holder", holder)
        .render()
    )
    
    output.write(text, f"license/{slug}/{id}.txt")
