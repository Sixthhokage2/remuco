"""Utilities and common stuff for wiki generator scripts."""

import codecs
import os
import re
import sys

import markdown
import commands

# -----------------------------------------------------------------------------
# useful attributes for wiki page generator scripts
# -----------------------------------------------------------------------------

_wiki_url = "http://code.google.com/p/remuco/wiki"

# wiki page file of current generator script (e.g. FooBar.py -> FooBar.wiki)
page_file = "%s.wiki" % os.path.splitext(sys.argv[0])[0]
page_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
page_url = "%s/%s" % (_wiki_url, page_name)

# -----------------------------------------------------------------------------
# helper methods for wiki page generator scripts
# -----------------------------------------------------------------------------

def file_at_rev(fname, revision):
    """Get content of a file from the remuco source at a specific revision."""
    
    cmd = "sh -c 'cd .. && hg cat -r %s %s'" % (revision, fname)
    ret, out = commands.getstatusoutput(cmd)
    if ret:
        print("failed to get content of %s at revision %s" % (fname, revision))
        sys.exit(1)

    return unicode(out, encoding="utf8")

def md2html(mdfile=None, md=None):
    """Convert a markdown file or string to HTML."""
    
    splitter = "<!-- WIKI -->"
    
    if md is None:
        with codecs.open(mdfile, 'r', 'utf-8') as fp:
            md = fp.read()
        
    html = markdown.markdown(md, extensions=["toc", "tables",])

    if splitter in html:
        html = html.split(splitter)[1]

    return html

def html2wiki(html, h1sep=False):
    """Polish HTML to look nice in a GC wiki.
    
    @keyword h1sep: if to preceed level 1 headings with a ruler
    
    """
    wiki = html
    
    # optionally preceed level 1 headers with a ruler
    if h1sep:
        wiki = re.sub(r'<h1.*?>', "-----\n<h1>", wiki)
        wiki = wiki.lstrip(" -\n") # remove top ruler
        

    # html headers to wiki headers
    for i in range(1,5):
        wiki = re.sub(r'<h%d.*?>' % i, "=" * i, wiki)
        wiki = re.sub(r'</h%d>' % i, "=" * i, wiki)

    wiki = wiki.replace("<pre><code>", "{{{\n")
    wiki = wiki.replace("</code></pre>", "}}}")
    
    # unescape characters escaped by markdown and taken literally by GC wiki
    for x, c in (("&lt;", "<"), ("&amp;", "&"), ("&gt;", ">")):
        wiki = wiki.replace(x, c)

    wiki = re.sub(r'\n *<', '\n<', wiki) # no ws before opening tag after lb
    wiki = re.sub(r'> *\n', '>\n', wiki) # no ws after closing tag before lb
    wiki = re.sub(r'\n *', '\n', wiki) # no whitespace after lb
    wiki = re.sub(r' *\n', '\n', wiki) # no whitespace before lb
    wiki = re.sub(r'<(/?)code>', r'<\1tt>', wiki) # code -> tt
    #wiki = re.sub(r'\n\n', '\n', wiki) # no double lb
    wiki = re.sub(r'<li>\n', '<li>', wiki) # no lb after <li>
    wiki = re.sub(r'\n</li>', '</li>', wiki) # no lb before </li>
    wiki = re.sub(r'<!--(.*)-->', r'<wiki:comment>\1</wiki:comment>', wiki)

    # escape WikiWords (CamelCase -> !CamelCase)
    re_ww_patt = r'(?<![a-z0-9])((?:[A-Z][a-z0-9]+){2,})(?![A-Za-z0-9"])'
    re_ww_repl = r'!\1'
    wiki = re.sub(re_ww_patt, re_ww_repl, wiki)
    
    # gc-wiki seems to ignore in-document links, make them full links
    wiki = re.sub(r'href="#', 'href="%s#' % page_url, wiki)

    return wiki

