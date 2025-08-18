# krobbi.github.io
[krobbi.github.io](https://krobbi.github.io/) is my personal GitHub Pages
website.

# Static Site Generation
The site is fully static, meaning all of its pages are stored on the server
with their content fully rendered. This improves page load performance and
compatibility at the expense of storing larger files with duplicate data.

The static files are generated from this repository using the extended edition
of [Hugo](https://gohugo.io/). This is the only dependency. The site is
automatically regenerated and deployed every time a `deploy/YYYY-MM-DD-rN`[^1]
tag is pushed to GitHub.

[^1]: Year, month, day, revision number.

GitHub Pages does not support server-side code, so static site generation is
useful for creating reusable components and page layouts without repeating
code[^2].

[^2]: In other words, it's DRY (don't repeat yourself).

An alternative would be to use JavaScript etc. and build the pages client-side.
This is sensible for web apps with many possible states, but for an ordinary
website this can cause issues for screen readers, web crawlers, and older
browsers.

# License
The content that appears on the generated site is copyrighted. Content from
other sites that is linked or embedded may be licensed differently. The code
used for generating the site may be used freely.

See [LICENSE.txt](/LICENSE.txt) for a full copy of the license text.
