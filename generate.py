import os
import shutil

OUTPUT_DIR: str = "out/"
"""The directory for outputting the site's content."""

def main() -> None:
    """Copy static files to the output directory."""
    
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    
    shutil.copytree("static/", OUTPUT_DIR)


if __name__ == "__main__":
    main()
