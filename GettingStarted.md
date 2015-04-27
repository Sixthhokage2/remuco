_**Using an older version (< 0.9.3) of Remuco?** See GettingStartedLegacy!_

<h1>Outline</h1>


---

# Quick Start #
<p>In case you can't wait, here's a quick start for using Remuco.</p>
<ol>
<li><a href='http://code.google.com/p/remuco/downloads/list'>Download</a> the latest Remuco package and extract it to a place of your<br>
choice.</li>
<li>In a terminal switch into <tt>/path/to/extracted-remuco-package</tt>.</li>
<li>Run <tt>sudo make install-PLAYER</tt> where <em>PLAYER</em> is the player you want to use<br>
with Remuco. Inspect the output for possibly missing requirements.</li>
<li>See section <a href='http://code.google.com/p/remuco/wiki/GettingStarted#Usage'>Usage</a> for how to enable the just installed player adapter.</li>
<li>Install the client, located in <tt>client/midp/app</tt> onto your phone.</li>
<li>Start the client and have fun.</li>
</ol>
<p>Got it working? Great! Otherwise follow the more detailed documentation below.</p>

---

# Requirements #
## General ##
<ul>
<li>Python ≥ 2.6 and < 3.0</li>
<li>Python modules <em>Image</em> (a.k.a. PIL), <em>logging</em>, <em>bluetooth</em>, <em>dbus</em>,<br>
<em>gobject</em> and <em>xdg</em></li>
</ul>
## Player specific ##
<ul>
<li><strong>Amarok:</strong>        Amarok ≥ 2.0</li>
<li><strong>Amarok14:</strong>      Amarok ≥ 1.4 and < 2.0, Python module <em>eyeD3</em></li>
<li><strong>Audacious:</strong>     Audacious ≥ 1.5.1 (2.1 has issues, 2.2 works again)</li>
<li><strong>Banshee:</strong>       Banshee ≥ 1.6.0</li>
<li><strong>Clementine:</strong>    Clementine ≥ 0.7.1 (older versions not tested)</li>
<li><strong>Exaile:</strong>        Exaile ≥ 0.3.1</li>
<li><strong>gmusicbrowser:</strong> gmusicbrowser ≥ 1.0.2</li>
<li><strong>MPD:</strong>           MPD ≥ 0.13.2, Python module <a href='http://mpd.wikia.com/wiki/!ClientLib:python-mpd'><em>mpd</em></a> (≥ 0.2)</li>
<li><strong>Quod Libet:</strong>    Quod Libet ≥ 2.2</li>
<li><strong>Rhythmbox:</strong>     Rhythmbox ≥ 0.11.5, Python module <em>gconf</em></li>
<li><strong>Songbird:</strong>      Songbird ≥ 1.2 with the <a href='http://addons.songbirdnest.com/addon/1626'>MPRIS Add-on</a> installed</li>
<li><strong>Totem:</strong>         Totem ≥ 2.22</li>
<li><strong>TVtime:</strong>        TVtime ≥ 0.9.11</li>
<li><strong>VLC:</strong>           VLC ≥ 0.9 with DBus control enabled (see <a href='http://wiki.remuco.googlecode.com/hg/images/exos/vlc-preferences.png'>screenshot</a>)</li>
<li><strong>XMMS2:</strong>         XMMS2 ≥ 0.5, Python module <em>xmmsclient</em> (≥ 0.5)</li>
</ul>
## MIDP Client ##
<p>The Remuco MIDP client requires a JavaME (J2ME) capable phone with MIDP ≥ 2.0<br>
and CLDC ≥ 1.1. To connect via Bluetooth the phone must support JSR-82 (Java<br>
Bluetooth API).  To check if your device matches the requirements take a look<br>
at the <a href='http://www.dpsoftware.org/filter.php'>FPC database</a> (add your phone if it's not listed yet).</p>
<p>Additionally check <a href='http://code.google.com/p/remuco/wiki/ClientDevices'>the list of phones successfully used with Remuco</a>.<br>
Once Remuco is running on your system, please help to extend this list by<br>
running the tool <em>remuco-report</em>.</p>
## Android Client ##
<p>The Android client requires Android ≥ 2.1 (though older versions may work).<br>
Check the <a href='http://code.google.com/p/remuco/wiki/ClientDevices'>client device list</a>, maybe your phone is already listed there.</p>

---

# Installation #
<p>To use Remuco you need to install one or more player adapters on your computer<br>
and a client for your mobile device.</p>
## Player Adapters ##
<p>You can either install <a href='http://code.google.com/p/remuco/wiki/DistributionPackages'>packages for your distribution</a> (may be a bit<br>
outdated) or you can <a href='http://code.google.com/p/remuco/downloads/list'>download</a> the latest Remuco release, extract it to a<br>
place of your choice and install one or more player adapters as follows:</p>
```
$ cd path/to/extracted-remuco-package
$ make help
... wow, good to know ...
$ sudo make install-PLAYER
... check output for missing requirements ...
```
<p>The last command installs the player adapter for <em>PLAYER</em> (replace this with a<br>
real name). After installation there are some files called <tt>install-...log</tt>.<br>
They are needed if you want to uninstall Remuco later.</p>
## MIDP Client ##
<p>The MIDP client application consists of 2 files:</p>
<ul>
<li><em>remuco.jar</em>: The client application to install on your mobile phone.</li>
<li><em>remuco.jad</em>: A descriptor file which is needed additionally by some phones<br>
for installation.</li>
</ul>
<p>The files are located in <tt>client/midp/app/</tt> (if you installed using<br>
distribution packages they probably are at <tt>/usr/share/remuco/client/</tt>).</p>
<p>The concrete steps to install the client depend on your phone. Usually the<br>
<em>JAR</em> file has to be sent or copied to the device. Some phones then already<br>
trigger the installation, others require to open the file with the device's<br>
file manager.</p>
<p>Next to the regular client you'll find special variants of the client<br>
in the above mentioned directory:</p>
<ul>
<li><em>motorola-fix</em>: Use this for older Motorola phones like ROKR E2, ROKR E6,<br>
MOTOZINE ZN5 and A1200e.</li>
<li><em>no-bluetooth</em>: A client without Bluetooth functionality. Some Windows based<br>
phones (using JBed) are known to require this client version.</li>
</ul>
## Android Client ##
<p>Remuco's Android client still is in it's beta phase, i.e. it generally works<br>
but yet requires some tweaks, features and fixes. That's why you won't find it<br>
in the Market. However, you'll find a test version in <tt>client/android/app</tt> to<br>
install manually (e.g. via USB) on your device.</p>
<p><strong>Note:</strong> You have to tune your phone settings to allow the installation of<br>
applications from untrusted sources (i.e. not from the market).</p>
<p>Additionally you may want to check the <a href='http://code.google.com/p/remuco/wiki/Android'>Android page in the wiki</a> for<br>
further information. There you'll also find some instructions how to build<br>
the client from source, in case you want to contribute or use the most recent<br>
version.</p>

---

# Usage #
## Amarok, Amarok14, Audacious, Clementine, Banshee, gmusicbrowser, Quod Libet, Songbird, VLC ##
<p>The player adapter can be started with the command <tt>remuco-PLAYER</tt> (replace<br>
<em>PLAYER</em> with a real player name).</p>
<p>A good choice is to set up <tt>remuco-PLAYER</tt> as a startup application when you<br>
log in to your desktop session. When the player is not running then the adapter<br>
is in sleep mode and won't eat much resources.</p>
<p><em>Note:</em> Remember to enable DBus control in VLC and to install the Songbird<br>
MPRIS Add-on (see above in section <a href='http://code.google.com/p/remuco/wiki/GettingStarted#Requirements'>Requirements</a>).</p>
## Exaile, Rhythmbox, Totem ##
<p>The player adapter actually is a plugin of the player. Thus it gets started<br>
automatically once you activate the Remuco plugin within the player.</p>
## MPD ##
<p>The player adapter can be started with the command <tt>remuco-mpd</tt>.</p>
<p>A good choice is to set up <tt>remuco-mpd</tt> as a startup application when you log<br>
in to your desktop session (in case MPD is already running at this time) or<br>
when MPD itself get's started. It mainly depends on your MPD setup.</p>
<p>If the player adapter is not running on the same computer as MPD have a look<br>
into the <a href='http://code.google.com/p/remuco/wiki/GettingStarted#Configuration'>Configuration</a> section below.</p>
## MPlayer ##
<p><strong>The lazy way:</strong>
Assuming both <em>mplayer</em> and <em>remuco-mplayer</em> are in your <em>PATH</em> variable, just<br>
run</p>
```
$ remuco-mplayer myawesomefile1 myawesomefile2 ... myawesomefileN
```
<p>and <em>remuco-mplayer</em> will call <em>mplayer</em> files it can find in that list.<br>
As of now, you cannot pass arguments to <em>mplayer</em>.</p>
<p><strong>The kludgy but one-off way:</strong>
Add a line to your <tt>~/.mplayer/config</tt> file, telling <em>mplayer</em> to read from the<br>
file <tt>.cache/remuco/mplayer.cmdfifo</tt> folder:</p>
```
echo "input=file=$HOME/.cache/remuco/mplayer/cmdfifo" >> ~/.mplayer/config
```
<p>This will allow you to control <em>mplayer</em> from the client, and should be done<br>
only once. Next start the adapter (as of now, you need to run the adapter<br>
before you run mplayer):</p>
```
$ remuco-mplayer
```
<p>To be able to get information from <em>mplayer</em> to clients, you need to pipe its<br>
output to a location known to remuco.</p>
```
$ mplayer mymovie.avi | tee $HOME/.cache/remuco/mplayer.statusfifo
```
<p>This should be all, you can now start the client. But note that you'll need to<br>
type that last command every time you want to play something with <em>mplayer</em>.</p>
<p>To make your life easier, add this script to your <tt>~/bin</tt> directory:</p>
```
[ -z $1 ] && echo "Usage: $0 file2 file2 ..." && exit 1

# if mplayer is installed elsewhere, change /usr/bin/mplayer to the correct location
/usr/bin/mplayer $@ | tee $HOME/.cache/remuco/mplayer.statusfifo
```
<p>Name this script <tt>~/bin/mplayer</tt> and make sure <tt>~/bin</tt> precedes <tt>/usr/bin</tt> in<br>
your <em>PATH</em> environment variable.</p>
## TVtime ##
<p>The player adapter can be started with the command <tt>remuco-tvtime</tt>.</p>
<p>For navigating in TVtime's menu with the Remuco client, the keys on the client<br>
have special functions when using the TVtime adapter:</p>
<table>
<thead>
<tr>
<th>Client Key</th>
<th>TVtime Key</th>
</tr>
</thead>
<tbody>
<tr>
<td>Playback</td>
<td><em>MENU_ENTER</em></td>
</tr>
<tr>
<td>Repeat</td>
<td><em>SHOW_MENU</em></td>
</tr>
<tr>
<td>Shuffle</td>
<td><em>SHOW_MENU</em></td>
</tr>
<tr>
<td>Previous</td>
<td><em>LEFT</em></td>
</tr>
<tr>
<td>Next</td>
<td><em>RIGHT</em></td>
</tr>
<tr>
<td>Vol. up</td>
<td><em>UP</em></td>
</tr>
<tr>
<td>Vol. down</td>
<td><em>DOWN</em></td>
</tr>
</tbody>
</table>
## XMMS2 ##
<p>The player adapter can be started with the command <tt>remuco-xmms2</tt>.</p>
<p>To let it start automatically when XMMS2 starts, create a symbolic link in the<br>
XMMS2 user startup script directory, for instance like this:</p>
```
$ ln -s `which remuco-xmms2` ~/.config/xmms2/startup.d/remuco-xmms2
```
## Client (MIDP and Android) ##
<p>Using the client should be quite obvious -- just start and use it ;) .</p>
## Report Tool ##
<p>Remuco comes with a tool called <em>remuco-report</em>. This tool submits information<br>
of seen Remuco client devices to the Remuco project. Help setting up a Remuco<br>
compatible device list, by using remuco-report! See the tool's man page for<br>
more information.</p>

---

# Configuration #
<p>Each player adapter can be configured in Remuco's configuration file placed in<br>
<tt>~/.config/remuco/remuco.cfg</tt>. This file is created automatically when a player<br>
adapter has been started the first time. The file contains a section <tt>DEFAULT</tt>
which defines options for <em>all</em> player adapters and additional sections for<br>
each player used with Remuco. These sections overwrite global options in<br>
<tt>DEFAULT</tt>and are used to define options which only make sense for specific<br>
players (look for options starting with <tt>x-</tt>).</p>
<p>Global options in section <tt>DEFAULT</tt> are documented within the configuration<br>
file. The player specific options are described below.</p>
## Amarok, Audacious, Songbird, VLC (MPRIS based adapters) ##
<ul>
<li><tt>x-playlist-jump-enabled</tt>:<br>
Toggle playlist jump action (default: <tt>0</tt>). If enabled, clients may jump<br>
within the player's playlist. This is disabled by default because the player<br>
interface does not support such an action. Remuco implements a dirty hack to<br>
realize that anyway but this only works on <em>non-dynamic</em> playlists. If you<br>
think that's okay, feel free to set a <em>1</em> here.</li>
</ul>
## MPD ##
<ul>
<li><tt>x-mpd-host</tt>:<br>
Host running MPD (default: <tt>localhost</tt>).</li>
<li><tt>x-mpd-port</tt>:<br>
Port used by MPD (default: <tt>6600</tt>).</li>
<li><tt>x-mpd-password</tt>:<br>
Password to use when connecting to MPD. Must be set if MPD is configured to<br>
restrict certain actions with a password requirement.</li>
<li><tt>x-mpd-music</tt>:<br>
Root directory of MPD's music directory (default: <tt>/var/lib/mpd/music</tt>).<br>
Used for searching cover art files and only works if MPD is at localhost.</li>
</ul>
<p>The defaults should work for most MPD setups.</p>
## MPlayer ##
<ul>
<li><tt>x-cmdfifo</tt>:<br>
FIFO file to use to send commands to MPlayer (default:<br>
<tt>~/.cache/remuco/mplayer.cmdfifo</tt>). For details see MPlayer usage in the<br>
<a href='http://code.google.com/p/remuco/wiki/GettingStarted#Usage'>Usage</a> section above.</li>
<li><tt>x-statusfifo</tt>:<br>
FIFO file to use to read output from MPlayer (default:<br>
~/.cache/remuco/mplayer.statusfifo). For details see MPlayer usage in the<br>
<a href='http://code.google.com/p/remuco/wiki/GettingStarted#Usage'>Usage</a> section above.</li>
</ul>

---

# Known Issues #
## Bluetooth service search ##
<p>On some phones the Remuco client does not find the player adapter services<br>
running on a computer. See the <a href='FAQ.md'>FAQ</a><a href='faq.md'>faq</a> for instructions how to fix this.</p>
<p><strong>BlackBerry devices:</strong> The default service search fails on BlackBerry devices.<br>
You have to manually set a service channel ≥ 7 in the client <em>and</em> in the<br>
player adapter configuration. For details see the <a href='http://code.google.com/p/remuco/wiki/FAQ'>FAQ</a>.</p>
## WiFi connections on BlackBerry devices ##
<p>On some BlackBerry devices (e.g. Bold 9000 or Pearl 8120) you need to set the<br>
option <tt>interface=wifi</tt> in a WiFi connection's configuration screen<br>
(<a href='http://wiki.remuco.googlecode.com/hg/images/exos/emulator-ifacewifi.png'>screenshot</a>). Otherwise the phone tries to connect using BIS (BlackBerry<br>
Internet Service) instead of the real WiFi interface.</p>
<p>Another user <a href='http://code.google.com/p/remuco/issues/detail?id=67'>reported</a> that the option <tt>deviceside=true</tt> had to be set in<br>
order to circumvent BES proxy connections. If it still fails, have a try with<br>
some other <a href='http://www.blackberry.com/developers/docs/5.0.0api/javax/microedition/io/Connector.html#socket'>options for WiFi connections on BlackBerry devices</a> and drop a<br>
note on the <a href='http://groups.google.com/group/remuco'>mailing list</a> in case you found a useful option.</p>
## Phones operated by AT&T Wireless or T-Mobile U.S. ##
<p>These operators have very restrictive access rights for third party JavaME<br>
applications. As a result it is likely that the Remuco client is not allowed to<br>
setup WiFi or Bluetooth connections. Read <a href='http://code.google.com/p/remuco/wiki/JavaMeApiPermissions'>all the details</a>.</p>
## Windows Mobile devices ##
<p>The default client fails to start on Windows Mobile devices using JBed for<br>
JavaME apps. Bluetooth is a problem here so you have to use the special client<br>
in the <tt>no-bluetooth</tt> sub-directory where the default client files are located.</p>
## Motorola devices ##
<p>Some Motorola devices (ROKR E2, ROKR E6, MOTOZINE ZN5 and A1200e) crash with<br>
the default client when adding a new Bluetooth connection. This is a bug in the<br>
devices' Java implementation. There's a special client version with a<br>
work-around for this bug. It's located in the <tt>motorola-fix</tt> sub-directory<br>
where the default client files are located.</p>
### Motorola K1 ###
<p>The default client fails on the K1 when using Bluetooth on the. A special<br>
client version in the <tt>motorola-k1-fix</tt> sub-directory fixes this problem.</p>

---

# Troubleshooting #
## General ##
<ul>
<li>If you experience any problems first have have a look into the log file of<br>
the player adapter your are using (<tt>~/.cache/remuco/PLAYER.log</tt> - replace<br>
<em>PLAYER</em> with a specific player name.</li>
<li>In case this does not help to find and solve the problem, enable debug log<br>
by setting the option <em>log-level</em> in <tt>~/.config/remuco/remuco.cfg</tt> to<br>
<em>DEBUG</em>. Restart the player adapter and inspect the log again.</li>
<li>If you are still lost, then it's time to <a href='http://code.google.com/p/remuco/wiki/Issues?tm=3'>ask for help</a>.</li>
</ul>
## MIDP Client ##
<ul>
<li>The client has a menu option called <em>Log</em> - check it.</li>
<li>If the client fails to start on your device, although it meets all<br>
requirements, have a look at <a href='http://code.google.com/p/remuco/wiki/MIDP'>MIDP</a> for possible reasons and solutions.</li>
</ul>
## Android ##
<ul>
<li>Go and fix it :-P (client is still in development).</li>
</ul>
