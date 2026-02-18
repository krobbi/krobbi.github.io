# krobbi.github.io
[krobbi.github.io](https://krobbi.github.io/) is my personal GitHub Pages
website.

The site is fully static, meaning all of its pages are stored on the server
with their content fully rendered. This improves page load performance and
compatibility at the expense of storing larger files with duplicate data.

The static files are generated from this repository using the extended edition
of [Hugo](https://gohugo.io/). This is the only dependency. The site is
regenerated and deployed when a `deploy/YYYY-MM-DD-rN`[^1] tag is pushed to
GitHub.

Hugo is currently locked on version
[`0.152.2`](https://github.com/gohugoio/hugo/releases/tag/v0.152.2) for this
project because it is the latest version where libsass is not deprecated. This
allows the site to be buit with a single dependency and no warnings.

[^1]: Year, month, day, revision number.

# License
See [LICENSE.txt](LICENSE.txt) for a full copy of the license text.
