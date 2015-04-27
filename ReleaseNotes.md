# Release 0.9.6 #
## Base ##
<ul>
<li>Always log errors to standard out (see <a href='http://code.google.com/p/remuco/issues/detail?id=170'><a href='https://code.google.com/p/remuco/issues/detail?id=170'>issue 170</a></a>).</li>
<li>Report tool for supported client devices is enabled again.</li>
</ul>
## Player adapters ##
<ul>
<li>New: Clementine</li>
<li>Various: make all OGG files visible in file browser (see <a href='http://code.google.com/p/remuco/issues/detail?id=155'><a href='https://code.google.com/p/remuco/issues/detail?id=155'>issue 155</a></a>).</li>
<li>MPD: more media browser actions for the MPD adapter</li>
<li>MPlayer: don't crash on failed/broken MPlayer connections (see<br>
<a href='http://code.google.com/p/remuco/issues/detail?id=156'><a href='https://code.google.com/p/remuco/issues/detail?id=156'>issue 156</a></a>).</li>
</ul>
## Clients ##
<ul>
<li>MIDP: new variant for Motorola K1 devices (see <a href='http://code.google.com/p/remuco/issues/detail?id=84'><a href='https://code.google.com/p/remuco/issues/detail?id=84'>issue 84</a></a>).</li>
<li>Android: automatically pause playback on incoming calls (see<br>
<a href='http://code.google.com/p/remuco/issues/detail?id=165'><a href='https://code.google.com/p/remuco/issues/detail?id=165'>issue 165</a></a>).</li>
<li>Android: support for list actions in media browser</li>
</ul>

---

# Release 0.9.5 #
## Player adapters ##
<ul>
<li>Exaile: Adapted to API changes in Exaile 0.3.2 (see <a href='http://code.google.com/p/remuco/issues/detail?id=118'><a href='https://code.google.com/p/remuco/issues/detail?id=118'>issue 118</a></a>).</li>
<li>gmusicbrowser: fix installation issue (see <a href='http://code.google.com/p/remuco/issues/detail?id=151'><a href='https://code.google.com/p/remuco/issues/detail?id=151'>issue 151</a></a>).</li>
<li>Totem: Adapted to recent API changes (see <a href='http://code.google.com/p/remuco/issues/detail?id=150'><a href='https://code.google.com/p/remuco/issues/detail?id=150'>issue 150</a></a>).</li>
</ul>

---

# Release 0.9.4 #
## Base ##
<ul>
<li>Remuco now requires Python 2.6.</li>
</ul>
## Player adapters ##
<ul>
<li>Banshee: Adapted to DBus-API changes in 1.6.0 (see <a href='http://code.google.com/p/remuco/issues/detail?id=126'><a href='https://code.google.com/p/remuco/issues/detail?id=126'>issue 126</a></a>).</li>
<li>New: gmusicbrowser</li>
</ul>
## Clients ##
<ul>
<li>Android: various new features and improvements and fixes (library support<br>
still is a bit buggy, but the basic features work pretty well).</li>
<li>Android: ready-to-install package included in the release tarball</li>
</ul>

---

# Release 0.9.3.1 #
<p>This is a minor bug fix release.</p>
## Base ##
<ul>
<li>Updated documentation.</li>
</ul>
## Player adapters ##
<ul>
<li>MPD: Fixed disc number formatting issue (see <a href='http://code.google.com/p/remuco/issues/detail?id=113'><a href='https://code.google.com/p/remuco/issues/detail?id=113'>issue 113</a></a>).</li>
</ul>

---

# Release 0.9.3 #
## Base ##
<ul>
<li>Improved local cover art detection.</li>
<li>Simplified configuration (one configuration file only, easier to adjust<br>
global and player specific options).</li>
<li>New menu navigation control support for video players (e.g. for DVD menus).</li>
</ul>
## Player adapters ##
<ul>
<li>Amarok, VLC: New playlist action for jumping to a specific position (must<br>
be enabled explicitly in the adapter configuration because it fails in<br>
dynamic playlists).</li>
<li>Banshee: Rating control finally works with Banshee 1.5.3.</li>
<li>Exaile: Fixed crash on library search with empty query.</li>
<li>Exaile: Added support for Exaile 3.1.</li>
<li>MPD: Sort track search results by album.</li>
<li>MPlayer: Improved command line interface.</li>
<li>MPlayer: Implement menu navigation feature.</li>
<li>New: Amarok 1.4, Quod Libet</li>
</ul>
## Clients ##
<ul>
<li>Original client is now called MIDP client.</li>
<li>MIDP: Power saving support (no communication when client is paused or<br>
minimized).</li>
<li>MIDP: Simplified action handling in media browser.</li>
<li>MIDP: New client variant for some Motorola phones (see <a href='http://code.google.com/p/remuco/issues/detail?id=46'><a href='https://code.google.com/p/remuco/issues/detail?id=46'>issue 46</a></a>).</li>
<li>MIDP: New client variant for some Windows phones using JBed (so you don't<br>
need to build it yourself anymore, see <a href='http://code.google.com/p/remuco/issues/detail?id=39'><a href='https://code.google.com/p/remuco/issues/detail?id=39'>issue 39</a></a>).</li>
<li>Android: Initial and experimental new client for Android devices.</li>
</ul>

---

# Release 0.9.2 #
## General ##
<ul>
<li>Progress of streams is now shown correctly (see <a href='http://code.google.com/p/remuco/issues/detail?id=36'><a href='https://code.google.com/p/remuco/issues/detail?id=36'>issue 36</a></a>).</li>
</ul>
## Base ##
<ul>
<li>Added option to player adapter config to set a fixed Bluetooth channel (see<br>
<a href='http://code.google.com/p/remuco/issues/detail?id=5'><a href='https://code.google.com/p/remuco/issues/detail?id=5'>issue 5</a></a> and <a href='http://code.google.com/p/remuco/issues/detail?id=31'><a href='https://code.google.com/p/remuco/issues/detail?id=31'>issue 31</a></a>).</li>
</ul>
## Player adapters ##
<ul>
<li>Songbird: Added Songbird adapter.</li>
<li>MPlayer: Added (roughly working) MPlayer adapter.</li>
<li>XMMS2: Made adapter work with XMMS2 0.6.</li>
<li>MPD: Added password configuration option (see <a href='http://code.google.com/p/remuco/issues/detail?id=29'><a href='https://code.google.com/p/remuco/issues/detail?id=29'>issue 29</a></a>).</li>
<li>Audacious: Made adapter work with Audacious 2.2 (see <a href='http://code.google.com/p/remuco/issues/detail?id=17'><a href='https://code.google.com/p/remuco/issues/detail?id=17'>issue 17</a></a>).</li>
<li>Rhythmbox: Added <em>Any</em> field to search mask.</li>
</ul>
## Client ##
<ul>
<li>Service search is now configurable to work around service search issues<br>
seen on some devices (see <a href='http://code.google.com/p/remuco/issues/detail?id=5'><a href='https://code.google.com/p/remuco/issues/detail?id=5'>issue 5</a></a>).</li>
<li>Added a client customization option which makes Remuco usable on Windows<br>
Mobile devices using JBed (only WiFi supported, see <a href='http://code.google.com/p/remuco/issues/detail?id=39'><a href='https://code.google.com/p/remuco/issues/detail?id=39'>issue 39</a></a>).</li>
<li>Cover art full screen mode now optionally stays enabled.</li>
<li>Made action handling more portable (see UI <a href='http://code.google.com/p/remuco/issues/detail?id=33'><a href='https://code.google.com/p/remuco/issues/detail?id=33'>issue 33</a></a>).</li>
<li>Added editor screen for existing connections.</li>
<li>Added optional authentication and encryption for Bluetooth connections.</li>
<li>Fixed minor memory leak bugs.</li>
<li>Ping interval is now configured on the client.</li>
</ul>

---

# Release 0.9.1.1 #
## Client ##
<ul>
<li>Fixed a memory leak bug on the client (which may have occurred when<br>
browsing item lists a lot).</li>
</ul>

---

# Release 0.9.1 #
## Base ##
<ul>
<li>Added client device info report tool <tt>remuco-report</tt>.</li>
</ul>
## Player adapters ##
<ul>
<li>Exaile: Added Exaile 3 adapter.</li>
<li>XMMS2: Enhanced media library browser.</li>
</ul>
## Client ##
<ul>
<li>Added options screen.</li>
<li>Optionally show detailed item information.</li>
<li>Size and type of cover art image are now configured on the client.</li>
<li>Item list page size is now configured on the client.</li>
<li>Pages in item lists can be selected by number (in addition to up/down<br>
navigation).</li>
</ul>

---

# Release 0.9.0 #
## General ##
<ul>
<li>Added paging mechanism to item lists to enable clients to browse very long<br>
item lists.</li>
<li>Added search feature.</li>
</ul>
## Base ##
<ul>
<li>Volume control optionally controls master volume.</li>
</ul>
## Client ##
<ul>
<li>Added touch-screen support.</li>
<li>Fullscreen cover art is now real fullscreen.</li>
<li>Dropped themes Korama and Chocolate, added 4 new themes for touchscreen<br>
devices.</li>
<li>Added several new icons.</li>
<li>Added script to automatically set up build environment.</li>
<li>Changed default key bindings.</li>
</ul>
## Player adapters ##
<ul>
<li>XMMS2: Implemented search feature.</li>
<li>MPD: Implemented search feature.</li>
<li>Rhythmbox: Implemented search feature.</li>
<li>Rhythmbox: Added repeat and shuffle control.</li>
</ul>

---

# Release 0.8.2.1 #
## General ##
<ul>
<li>Fixed obsolete client installation in <tt>setup.py</tt>.</li>
</ul>
## Player adapters ##
<ul>
<li>Totem: Adapted to Totem 2.26.</li>
</ul>

---

# Release 0.8.2 #
## Base ##
<ul>
<li>Fixed Python path issue in Ubuntu Jaunty.</li>
</ul>
## Player adapters ##
<ul>
<li>VLC: Added player adapter for VLC.</li>
<li>TVtime: Added player adapter for TVtime.</li>
<li>Banshee: Added seek support.</li>
<li>Rhythmbox: Added action to directly jump to items somewhere in the library.</li>
</ul>
## Client ##
<ul>
<li>Quick reconnect when connection is broken.</li>
<li>Removed some unused icons (smaller JAR size).</li>
<li>Logo size configurable in build process.</li>
</ul>

---

# Release 0.8.1 #
## General ##
<ul>
<li>Various minor technical improvements (as always :).</li>
</ul>
## Base ##
<ul>
<li>base: Added option for WiFi port.</li>
<li>base: Added options for size and type of images sent to clients.</li>
<li>base: Fixed a bug concerning the system shutdown command.</li>
</ul>
## Player adapters ##
<ul>
<li>MPD: Added player adapter for MPD.</li>
</ul>
## Client ##
<ul>
<li>Full screen control enabled.</li>
<li>Fixed a color bug in theme Karoma.</li>
<li>Fixed some drawing issues on Nokia 5310.</li>
<li>More accurate list icon size detection.</li>
<li>Action execution improved.</li>
<li>Build process now works completely without WTK.</li>
<li>Emulation with MicroEmu now possible with other skins.</li>
</ul>

---

# Release 0.8.0.1 #
## General ##
<ul>
<li>No additional features, just internal adjustments.</li>
<li>Added GPL header to source files.</li>
<li>Replaced nested make files and setup.py by global setup.py.</li>
<li>Include client source in tarball.</li>
</ul>
## Base ##
<ul>
<li>Replace Python module 'md5' by 'hashlib'.</li>
</ul>
## Client ##
<ul>
<li>Set 'Vilanco' as default theme ('Chocolate' is too big for some devices).</li>
</ul>

---

# Release 0.8.0 #
## General ##
<ul>
<li>Merged client and server side components into one package.</li>
<li>For that reason this change log is a fresh one.</li>
<li>The changes from 0.7 to 0.8 are just to many to list them here.</li>
</ul>