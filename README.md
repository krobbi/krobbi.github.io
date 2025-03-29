# krobbi.github.io
_My GitHub Pages website._  
__Copyright &copy; 2024-2025 Chris Roberts__ (Krobbizoid).  
_All rights reserved._

# Contents
1. [About](#about)
2. [Generating](#generating)
3. [License](#license)

# About
krobbi.github.io is a GitHub Pages website hosted at https://krobbi.github.io.
The site contains:
* A homepage.
* A 404 page.
* A page listing software license texts.
* Software license texts hosted in plaintext.
* CSS stylesheets.
* Favicon images.

# Generating
The site is fully static, meaning all of its pages are stored on the server
with their contents fully rendered. This improves page load performance and
compatibility at the expense of storing larger files with duplicate data.

The site's content is generated using the [Python](https://www.python.org)
script `generate.py` in the root of this repository. The script requires the
packages listed in `requirements.txt` installed to run correctly.

The script generates the site's content in the `out/` directory and cleans the
directory if it already exists. Currently the script copies the static files
from `static/`, and generates CSS stylesheets from the SCSS in `scss/`.

# License
The site's content is released under an all rights reserved license. The code
used for generating the site may be used freely.

See [LICENSE.txt](./LICENSE.txt) for a full copy of the license text.
