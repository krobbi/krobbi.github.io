import os
import shutil

from pathlib import Path

OUTPUT_PATH: Path = Path("out/")
"""The directory for outputting the site's content."""

def main() -> None:
    """Copy static files to the output directory."""
    
    if os.path.exists(OUTPUT_PATH):
        shutil.rmtree(OUTPUT_PATH)
    
    shutil.copytree("static/", OUTPUT_PATH)


if __name__ == "__main__":
    main()
