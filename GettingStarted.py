"""Generator script for GettingStarted.wiki

Uses the README from the Remuco source repository to generate the
GettingStarted content.

"""

import codecs

import wutil

TMPL = """#summary How to install and use Remuco
#labels Documentation,Featured,Generated

_*Using an older version (< 0.9.3) of Remuco?* See GettingStartedLegacy!_

<h1>Outline</h1>
<wiki:toc max_depth="1"/>
-----
%s
"""

# the revision below needs to get changed to a fixed revision if README at
# tip significantly diverged from README of the latest release
md = wutil.file_at_rev("doc/README", "0.9.6")
html = wutil.md2html(md=md)
wiki = wutil.html2wiki(html, h1sep=True)

with codecs.open(wutil.page_file, 'w', "utf-8") as fp:
    fp.write(TMPL % wiki)

