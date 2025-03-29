import os

from pathlib import Path

import sass

import output

def main():
    """Generate the site's content."""
    
    output.reset()
    
    for entry in os.scandir("styles"):
        text = sass.compile(filename=entry.path, output_style="compressed")
        path = (Path("css") / entry.name).with_suffix(".css")
        output.write(text, path)


if __name__ == "__main__":
    main()
