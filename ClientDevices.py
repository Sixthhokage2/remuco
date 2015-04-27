"""Generator script for ClientDevices.wiki."""

from __future__ import with_statement

import re
import urllib

import wutil

TMPL = """#summary List of client devices successfully used with Remuco
#labels Documentation,Generated

Thanks to all users who have contributed to this list!

_You can extend the list by using the tool remuco-report._

**Note:** Previously this list has been longer because devices have been
distinguished also by minor version numbers. Unfortunately, this resulted in a
page size exceeding the allowed limit. For this reason the list has been made
more compact now, by dropping some details.

%s

<p>Last update: %s</p>
"""

# -----------------------------------------------------------------------------
# get report data
# -----------------------------------------------------------------------------

DB = "http://remuco.sourceforge.net/device.db"
DB_LOCAL = "%s.db" % wutil.page_name

try:
    #pass
    urllib.urlretrieve(DB, DB_LOCAL)
except IOError, e:
    raise StandardError("failed to download device db (%s)" % e)

with open(DB_LOCAL, "r") as fp:
    db = fp.read()
    
db = re.sub(r'[<>&]', '', db)
db = [entry.strip() for entry in db.split("\n")]
db = [entry for entry in db if entry and not entry.startswith("#")]

reports = []

for entry in db:
    report = {}
    items = [item.strip() for item in entry.split(",")]
    items = [item for item in items if item]
    for item in items:
        key, value = item.split(":", 1)
        report[key] = value
    reports.append(report)

ts_last = "0" # last update
for report in reports:
    ts = report.get("ts", "0")
    if ts > ts_last:
        ts_last = ts

# -----------------------------------------------------------------------------
# html2wiki device names
# -----------------------------------------------------------------------------

NAME_MAP = (
    (r"^A1200e", "Motorola A1200e"),
    (r"^A45 ", "Motorola A45 "),
    (r"^E2$", "Motorola ROKR E2"),
    (r"^L6i$", "Motorola SLVR L6i"),
    (r"^L7$", "Motorola SLVR L7"),
    (r"^K1$", "Motorola KRZR K1"),
    (r"^V3", "Motorola RAZR V3"),
    (r"^MOTORAZRV9$", "Motorola RAZR V9"),
    (r"^RAZRV", "Motorola RAZR V"),
    (r"^GT-", "Samsung GT-"),
    (r"^S8000", "Samsung S8000"),
    (r"^S5230", "Samsung S5230"),
    (r"^SGH", "Samsung SGH"),
    (r"^[0-9\.]+/SamsungSGH", "Samsung SGH"),
    (r"^SEC-SGH", "Samsung SGH"),
    (r"SAMSUNG", "Samsung"),
    (r"^Samsung(/|-|:)", "Samsung "),
    (r'"GT-I', '"Samsung GT-I'), # android
    (r"^Vodafone/1.0/LG-([A-Za-z0-9]+)", r"LG \1/Vodafone/1.0"),
    (r"^Vodafone/1.0/GT-([A-Za-z0-9]+)", r"Samsung GT-\1/Vodafone/1.0"),
    (r"^LG/([A-Z]+)", r"LG \1"),
    (r"^LG-", "LG "),
    (r"^LGGT", "LG GT"),
    (r"^wtk-emulator$", "Emulator: Sun WTK"),
    (r"MicroEmulator(-2.0)?", "Emulator: MicroEmu"),
    (r"-Orange", "/Orange"),
    (r"^SIE-", "Siemens "),
    (r"HTC_Touch_HD_", "HTC Touch HD "),
    (r"Polaris", "HTC Polaris"),
)

for report in reports:
    for patt, repl in NAME_MAP:
        report["name"] = re.sub(patt, repl, report["name"])
    name = report["name"]
    report["name"] = report["name"].split("/")[0]

# -----------------------------------------------------------------------------
# collapse reports to preliminary table rows
# -----------------------------------------------------------------------------

reports.sort(cmp=lambda x,y: cmp(x["name"], y["name"]))

#for report in reports: print report["name"]

VERSIONS = ["0.9.1", "0.9.2", "0.9.3", "0.9.4", "0.9.5", "0.9.6"]
DEVINFOS = ["Touchscreen"]
COLUMNS = ["name"] + VERSIONS + DEVINFOS


def row_tmpl():
    tmpl = {}
    for ver in VERSIONS:
        tmpl[ver] = set()
    for dinfo in DEVINFOS:
        tmpl[dinfo] = set()
    return tmpl

rows = {}
for report in reports:
    name = report["name"]
    row = rows.get(name, row_tmpl())
    row["name"] = name
    if report["version"] in row:
        row[report["version"]].add(report["conn"])
    else:
        print("warning: unknown version %s" % report["version"])
    row["Touchscreen"].add(report["touch"])
    #row["UTF8"].add(report["utf8"])
    rows[name] = row

REPLACEMENTS = {
    "bluetooth": '<img src="http://wiki.remuco.googlecode.com/hg/images/bluetooth_16.png" alt="Bluetooth" title="Bluetooth"/>',
    "wifi": '<img src="http://wiki.remuco.googlecode.com/hg/images/wifi_16.png" alt="WiFi" title="WiFi"/>',
    "bluetooth,wifi": '<img src="http://wiki.remuco.googlecode.com/hg/images/bluetooth_16.png" alt="Bluetooth" title="Bluetooth"/> <img src="http://wiki.remuco.googlecode.com/hg/images/wifi_16.png" alt="WiFi" title="WiFi"/>',
    "yes": '<font color="green">YES</font>', #"&#149;"
    "no": '<font color="red">NO</font>',
    "no,yes": '<font color="orange">MAYBE</font>',
    "": '<font color="gray">?</font>',
}

for name, row in rows.items():
    row = rows[name]
    for key, value in row.items():
        if isinstance(value, set):
            value = list(value)
            value.sort()
            value = ",".join(value)
        row[key] = REPLACEMENTS.get(value, value)
    #print name, row    

# -----------------------------------------------------------------------------
# build html table
# -----------------------------------------------------------------------------

html = ''

### table header ###

html += '<table border="1" cellpadding="4">\n'
html += '<tr align="center">\n'
html += '<th rowspan="2">Device</th>\n'
for ver in VERSIONS:
    html += '<th rowspan="2">Client %s</th>\n' % ver
html += ('<th colspan="%d">Device Features</th>\n' %
         (len(DEVINFOS)))
html += '</tr>'
html += '<tr align="center">\n'
for dinfo in DEVINFOS:
    html += '<th>%s</th>\n' % dinfo
html += '</tr>\n'

### table body ###

names = list(rows.keys())
names.sort()

for name in names:
    row = rows[name]
    html += '<tr align="center">\n'
    for col in COLUMNS:
        val = row[col]
        if col == "name":
            html += '<td align="left">%s</td>\n' % wutil.html2wiki(val)
        else:
            html += '<td>%s</td>\n' % val
    html += '</tr>\n'

### table footer ###

html += '</table>\n'

# -----------------------------------------------------------------------------
# write page
# -----------------------------------------------------------------------------

with open(wutil.page_file, 'w') as fp:
    fp.write(TMPL % (html, ts_last))

