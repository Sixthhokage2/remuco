"""Generator script for News.wiki

News are written in markdown in News.md. This script converts the markdown
written news into HTML and puts the HTML content into News.wiki. Additionally
it creates the RSS feed file News.xml (especially this is easier if news are
written in markdown and not in GC's wiki markup).
"""

from __future__ import with_statement

import datetime
from itertools import ifilter
import os.path
import re

import markdown
import PyRSS2Gen as rss

import wutil

TMPL = """#summary Project news and release announcements
#labels Generated

[http://wiki.remuco.googlecode.com/hg/News.xml http://wiki.remuco.googlecode.com/hg/images/rss.png]

%s

Older news are available at [http://sourceforge.net/news/?group_id=166515 SourceForge].
"""

html = wutil.md2html(mdfile="%s.md" % os.path.splitext(wutil.page_file)[0])
wpage = wutil.html2wiki(html)

with open(wutil.page_file, 'w') as fp:
    fp.write(TMPL % wpage)

# rss feed:

items = re.split(r'<h4.*?>([0-9]+ +\w+ +[0-9]+ +- +.*)</h4>', html)
items = [i.strip("\n ") for i in items]
items = [i for i in items if i]

news = []
odd = lambda x: not items.index(x) % 2 # ifilter keyfunc
even = lambda x: items.index(x) % 2 # ifilter keyfunc
last_build_date = None
for header, content in zip(ifilter(odd, items), ifilter(even, items)):
    anchor = header.replace(" ", "_").replace(",", "_,") # GC specific
    link = "%s#%s" % (wutil.page_url, anchor)
    date, title = [x.strip() for x in header.split("-", 2)]
    date = datetime.datetime.strptime(date, "%d %B %Y")
    last_build_date = last_build_date or date
    news.append(rss.RSSItem(title=title, description=content, link=link,
                            pubDate=date, guid=rss.Guid(link, True),
                            author="Remuco Team"))
        
FEED_NAME = "Remuco"
FEED_DESC = ("Project news and release announcements for Remuco, a "
             "wireless remote control for media players.")
FEED_IMG = "http://code.google.com/p/remuco/logo?logo_id=1251976392"
FEED_AUTHOR = "Oben Sonne"

feed = rss.RSS2(title=FEED_NAME, link=wutil.page_url, description=FEED_DESC,
                lastBuildDate=last_build_date, items=news,
                image=rss.Image(FEED_IMG, FEED_NAME, wutil.page_url))

with open("%s.xml" % wutil.page_name, 'w') as fp:
    feed.write_xml(fp)
