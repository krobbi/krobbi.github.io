import os
import shutil

from pathlib import Path

_OUTPUT_DIR = Path("out")
"""The path for outputting the site's content."""

def reset():
    """Clean the output directory and output the site's static files."""
    
    if os.path.exists(_OUTPUT_DIR):
        shutil.rmtree(_OUTPUT_DIR)
    
    shutil.copytree("static", _OUTPUT_DIR)


def write(text: str, path: Path):
    """Write text content to an output file by its path."""
    
    path = _OUTPUT_DIR / path
    
    os.makedirs(path.parent, exist_ok=True)
    
    with open(path, "w") as file:
        file.write(text)
