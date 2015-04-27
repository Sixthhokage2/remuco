# -*- coding: UTF-8 -*-

"""Generator script for Featues.wiki."""

from __future__ import with_statement

from itertools import cycle

import wutil

# =============================================================================
# Feature meta information
# =============================================================================

TYPE_DESCS = {
    "ct" : "Control features available on clients",
    "dp" : "Information shown on clients",
    "mb" : "Browsing features available on clients",
}

FEATURE_DESCS = [
    ("ct_playback", "Toggle playing, skip to next or previous track"),
    ("ct_volume", "Adjust volume"),
    ("ct_seek", "Seek forward and backward in current track"),
    ("ct_rate", "Rate currently played track"),
    ("ct_repeat", "Toggle repeat mode"),
    ("ct_shuffle", "Toggle shuffle mode"),
    ("ct_tag", "Label currently played track"),
    ("ct_navi", "Menu navigation (DVD-like)"),
    ("dp_playback", "Playback state"),
    ("dp_volume", "Volume level"),
    ("dp_progress", "Playback progress"),
    ("dp_art", "Art image related to currently played track"),
    ("dp_meta", "Artist, album, title, ... of currently played track"),
    ("dp_rating", "Rating of currently played track"),
    ("dp_repeat", "Repeat mode"),
    ("dp_shuffle", "Shuffle mode"),
    ("mb_playlist", "Browse the playlist and apply actions to playlist tracks"),
    ("mb_queue", "Browse the play queue and apply actions to queue tracks"),
    ("mb_mlib", "Browse the media library and apply actions to lists and tracks within the media library"),
    ("mb_search", "Search the media library media and apply actions to tracks in a search result"),
    ("mb_files", "Browse the local file system and apply actions to files"),
]

# =============================================================================
# Feature maps of players
# =============================================================================

AMAROK = {
    "name" : "Amarok",
    "version" : "2.0",
    "link" : "http://amarok.kde.org/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : ["Remove tracks from playlist"],
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : ["Append files to playlist", "Append files to playlist and play them immediately"],
}

AMAROK14 = {
    "name" : "Amarok-1.4",
    "version" : "1.4",
    "link" : "http://amarok.kde.org/",
    "ct_playback" : True,
    "ct_seek" : False,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : ["Jump in playlist", "Remove tracks from playlist"],
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : ["Append files to playlist", "Append files to playlist and play them immediately"],
}

AUDACIOUS = {
    "name" : "Audacious",
    "version" : "1.5.1",
    "link" : "http://audacious-media-player.org/",
    "notes" : ["There are some known problems with Audacious 2.1, see [http://code.google.com/p/remuco/issues/detail?id=17 this issue]. Audacious 2.2 and newer works without problems."],
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : ["Remove tracks from playlist"],
    "mb_queue" : False,
    "mb_mlib" : ["Append track to active playlist"],
    "mb_search" : ["Append track to active playlist"],
    "mb_files" : False
}

BANSHEE = {
    "name" : "Banshee",
    "version" : "1.5.3",
    "link" : "http://banshee-project.org/",
    "notes" : ["Banshee < 1.5.3 works, but without rating support."],
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : False,
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : False
}

EXAILE = {
    "name" : "Exaile",
    "version" : "0.3.1",
    "link" : "http://exaile.org/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : ["Remove tracks from playlist", "Jump in playlist", "Enqueue playlist tracks"],
    "mb_queue" : ["Remove tracks from queue", "Jump to a specific queue position"],
    "mb_mlib" : ["Append track to active playlist", "Enqueue selected tracks", "Remove tracks from a list", "Create new playlist from selected tracks", "Repopulate active playlist with selected tracks", "Open and play stored playlists", "Switch between open playlists", "Close open playlists"],
    "mb_search" : ["Append selected tracks to active playlist", "Enqueue selected tracks", "Repopulate active playlist with selected tracks", "Create new playlist from selected tracks"],
    "mb_files" : False
}

GMUSCBROWSER = {
    "name" : "Gmusicbrowser",
    "version" : "1.0.2",
    "link" : "http://gmusicbrowser.org/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : False,
    "ct_shuffle" : False,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : False,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : False,
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : False,
}

MPD = {
    "name" : "MPD",
    "version" : "1.13.2",
    "link" : "http://musicpd.org/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : ["Remove tracks from playlist", "Jump in playlist"],
    "mb_queue" : False,
    "mb_mlib" : ["Append track to active playlist", "Repopulate active playlist with selected tracks", "Play a stored playlist", "Append a stored playlist to active playlist"],
    "mb_search" : ["Append track to active playlist", "Repopulate active playlist with selected tracks"],
    "mb_files" : False
}

MPLAYER = {
    "name" : "MPlayer",
    "version" : "1.0",
    "link" : "http://www.mplayerhq.hu/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : False,
    "ct_shuffle" : False,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : True,
    "dp_playback" : True,
    "dp_repeat" : False,
    "dp_shuffle" : False,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : False,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : False,
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : ["Append files to playlist", "Replace current playlist by a new file"]
}

QUODLIBET = {
    "name" : "Quod-Libet",
    "version" : "2.2",
    "link" : "http://code.google.com/p/quodlibet/",
    "ct_playback" : True,
    "ct_seek" : False,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : False,
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : False
}

RHYTHMBOX = {
    "name" : "Rhythmbox",
    "version" : "0.11.5",
    "link" : "http://www.rhythmbox.org/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : ["Enqueue selected tracks", "Jump in playlist"],
    "mb_queue" : ["Remove tracks from queue", "Jump to a specific queue position"],
    "mb_mlib" : ["Enqueue selected tracks", "Activate another playlist"],
    "mb_search" : ["Enqueue selected tracks"],
    "mb_files" : False
}

SONGBIRD = {
    "name" : "Songbird",
    "version" : "1.2",
    "link" : "http://www.getsongbird.com/",
    "notes" : ["Requires Songbird MPRIS Add-on"],
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : False,
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : False
}

TOTEM = {
    "name" : "Totem",
    "version" : "2.22",
    "link" : "http://www.gnome.org/projects/totem/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : False,
    "ct_shuffle" : False,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : False,
    "dp_shuffle" : False,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : ["Remove tracks from playlist"],
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : ["Append files to playlist", "Append files to playlist and play them immediately"]
}

TVTIME = {
    "name" : "TVtime",
    "version" : "0.9.11",
    "link" : "http://tvtime.sourceforge.net/",
    "ct_playback" : True,
    "ct_seek" : False,
    "ct_repeat" : False,
    "ct_shuffle" : False,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_navi" : False,
    "ct_tag" : False,
    "dp_playback" : False,
    "dp_repeat" : False,
    "dp_shuffle" : False,
    "dp_volume" : True,
    "dp_progress" : False,
    "dp_art" : False,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : ["Jump to another channel"],
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : False
}

VLC = {
    "name" : "VLC",
    "version" : "0.9",
    "link" : "http://www.videolan.org/vlc/",
    "notes" : ["DBus control must be enabled in VLC"],
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : True,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : False,
    "ct_tag" : False,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : True,
    "dp_shuffle" : True,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : False,
    "mb_playlist" : False,
    "mb_queue" : False,
    "mb_mlib" : False,
    "mb_search" : False,
    "mb_files" : ["Append files to playlist", "Repopulate current playlist with selected files"],
}

XMMS2 = {
    "name" : "XMMS2",
    "version" : "0.5",
    "link" : "http://wiki.xmms2.xmms.se/",
    "ct_playback" : True,
    "ct_seek" : True,
    "ct_repeat" : False,
    "ct_shuffle" : True,
    "ct_volume" : True,
    "ct_rate" : True,
    "ct_tag" : True,
    "ct_navi" : False,
    "dp_playback" : True,
    "dp_repeat" : False,
    "dp_shuffle" : False,
    "dp_volume" : True,
    "dp_progress" : True,
    "dp_art" : True,
    "dp_meta" : True,
    "dp_rating" : True,
    "mb_playlist" : ["Remove tracks from playlist", "Jump in playlist"],
    "mb_queue" : False,
    "mb_mlib" : ["Append tracks to active playlist", "Select tracks to play next", "Change active playlist"],
    "mb_search" : ["Append tracks to playlist", "Select tracks to play next"],
    "mb_files" : False
}

# =============================================================================
# List of all players
# =============================================================================

PLAYERS = [AMAROK, AMAROK14, AUDACIOUS, BANSHEE, EXAILE, GMUSCBROWSER, MPD,
           MPLAYER, QUODLIBET, RHYTHMBOX, SONGBIRD, TOTEM, TVTIME, VLC, XMMS2]

# =============================================================================
# Builders
# =============================================================================

BASE_URL_IMG = "http://wiki.remuco.googlecode.com/hg/images"

def feature_type_section(player, feature_type):
    """Build HTML content of a feature type section in a player section."""

    html = '\n'
    html += '<b>%s:</b>' % TYPE_DESCS[feature_type]
    html += '\n'

    html += '<ul>'

    html_list = ''

    for feature_desc in FEATURE_DESCS:

        feature_id = feature_desc[0]

        if not feature_id.startswith(feature_type):
            continue

        if feature_id in player and player[feature_id]:
            html_list += '<li>%s</li>' % feature_desc[1]

    html += html_list or '<li>None</li>'

    html += '</ul>\n'

    return html


def player_section(player):
    """Build HTML content of a player section."""

    html = ''

    # visual player separator
    spacer = '<font color="#ffffff" font-size="1">x</font>'
    html += '%s\n<hr/>\n%s\n' % (spacer, spacer)

    # table for icon, name and up-link
    html += '<table>\n'
    html += '<tr valign="middle">\n'
    html += '<td align="center">\n'
    html += '<a href="%s">' % player["link"]
    name = player["name"]
    img = "%s/%s.png" % (BASE_URL_IMG, name.lower())
    html += ('<img border="0" width="48" src="%s" alt="%s Website" '
             'title="%s Website"/>' %
             (img, name, name))
    html += '</a>\n'
    html += '</td>\n'
    html += '<td align="left">\n'
    html += '<b>%s</b>\n' % player["name"]
    html += '</td>\n'
    html += '<td align="right" width="30px">\n'
    html += '<a href="%s#">up</a>\n' % wutil.page_url
    html += '</td>\n'
    html += '<td align="left">\n'
    html += '<font color="#ffffff">\n'
    html += '=== %s ===\n' % player["name"]
    html += '</font>\n'
    html += '</td>\n'
    html += '</tr>\n'
    html += '</table>\n'

    html += '<ul>'
    html += '<li><i>Requires %s ≥ %s</i></li>' % (player["name"], player["version"])
    notes = player.get("notes", [])
    if notes:
        for note in notes:
            html += '<li>%s</li>' % note
    html += '</ul>'

    # feature sections
    for feature_type in ("ct", "dp" ,"mb"):
        html += feature_type_section(player, feature_type)

    return html

def details():
    """Build HTML content of all player feature details."""

    html = ''
    for player in PLAYERS:
        html += player_section(player)
        html += '<p/>\n'
    return html

def overview():
    """Build HTML content of the player overview section."""

    columns = 6
    rows = []
    for i, player in enumerate(PLAYERS):
        if i % columns == 0:
            rows.append([])
        rows[-1].append(player)
    rows[-1].extend([None] * (columns - len(rows[-1])))
    html = ''
    for row in rows:
        html += '<table border="0" cellpadding="3" valign="middle" width="800">\n'
        html += '<tr align="center">\n'
        for player in row:
            html += '<td width="%d%%">' % (100 // columns)
            if player is None:
                html += ' </td>\n'
                continue
            name = player["name"]
            img = "%s/%s.png" % (BASE_URL_IMG, name.lower())
            html += '<a href="%s#%s">' % (wutil.page_url, name)
            html += ('<img border="0" width="32" src="%s" alt="%s Features" title="%s Features"/>' %
                     (img, name, name))
            html += '</a>'
            html += '</td>\n'
        html += '</tr>\n'
        html += '<tr align="center">\n'
        for player in row:
            html += '<td>'
            if player is None:
                html += ' </td>\n'
                continue
            html += '<b>%s</b><br/>' % player["name"]
            html += '</td>\n'
        html += '</tr>\n'
        html += '</table>\n\n'

    return html

# =============================================================================
# Page
# =============================================================================

TMPL = """#summary Supported media players and respective features
#labels Featured,Generated

_*Note:* The MIDP client supports all features listed here. The experimental
Android client may miss a few._

%s

<table width="800"><tr><td>
%s
</td></tr></table>
"""

with open(wutil.page_file, 'w') as fp:
    fp.write(TMPL % (overview(), details()))
