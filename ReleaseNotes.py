"""Generator script for ReleaseNotes.wiki."""

from __future__ import with_statement

import os.path

import markdown

import wutil

TMPL = """#summary Remuco release notes and changes
#labels Featured,Generated

%s
"""

md = wutil.file_at_rev("doc/CHANGES", "default")
html = wutil.md2html(md=md)
wiki = wutil.html2wiki(html, h1sep=True)

with open(wutil.page_file, 'w') as fp:
    fp.write(TMPL % wiki)

