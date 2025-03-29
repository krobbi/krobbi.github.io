import os
import shutil

from pathlib import Path

import sass

def main():
    output_dir = Path("out")
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    shutil.copytree("static", output_dir)
    
    css_dir = output_dir / "css"
    os.mkdir(css_dir)
    
    for entry in os.scandir("scss"):
        css = sass.compile(filename=entry.path, output_style="compressed")
        
        with open((css_dir / entry.name).with_suffix(".css"), "w") as file:
            file.write(css)


if __name__ == "__main__":
    main()
