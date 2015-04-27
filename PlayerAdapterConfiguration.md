<font color='red'>
<i><b>This documentation refers to Remuco ≤ 0.9.2. Since 0.9.3 the<br>
player adapter configuration documentation is part of GettingStarted.</b></i>
</font>


---


<h1>Overview</h1>


Each player adapter can be configured by its configuration file placed in <tt>~/.config/remuco/<i>PLAYER</i>/conf</tt>. This file along with default values is created automatically when a player adapter has been started the first time.

# General Configuration Options #

## Connectivity ##

```
bluetooth-enabled = 1
```
  * Specifies if to enable Bluetooth connections.
  * Possible values: _0_, _1_

```
bluetooth-channel = 0
```
  * Specifies the channel to use for Bluetooth connections.
  * _0_ means the next free channel is selected automatically
  * Possible values: _1 - 30_

```
wifi-enabled = 1
```
  * Specifies if to enable WiFi connections.
  * Possible values: _0_, _1_

```
wifi-port = 34271
```
  * Specifies the port to use for WiFi (Inet) connections.
  * Must be changed to enable Remuco for [multiple players simultaneously](FAQ#Can_I_use_Remuco_for_multiple_players_simultaneously?.md) when using WiFi connections.
  * Possible values: _a free port_

## File Browser ##

```
file-browser-root-dirs = 
```
  * A colon separated list of root directories to show in a client's file browser.
  * This option is only relevant if a player adapter supports the [file browser feature](Features.md).
  * By default the root dirs are one or more of _XDG\_MUSIC\_DIR_, _XDG\_VIDEOS\_DIR_ or _XDG\_PICTURES\_DIR_ (see <tt>~/.config/user-dirs.dirs</tt>), depending on the mime types a player supports.
  * If none of the _XDG_ directories make sense and no root directory is set here, then the user home directory is used as a fallback.
  * Example value: <tt>/media/Music:/home/john/stuff</tt>

```
file-browser-show-extensions = 0
```
  * Specifies if to show file name extensions in the client's file browser.
  * This option is only relevant if a player adapter supports the [file browser feature](Features.md).
  * Possible values: _0_, _1_

```
file-browser-enabled = 1
```
  * Specifies if to enable the file browser in clients.
  * This option is only relevant if a player adapter supports the [file browser feature](Features.md).
  * Possible values: _0_, _1_

```
file-browser-use-xdg-user-dirs = 1
```
  * Specifies if to make use of the XDG variables mentioned above when setting up the list of file browser root directories.
  * This option is only relevant if a player adapter supports the [file browser feature](Features.md).
  * Possible values: _0_, _1_

## Miscellaneous ##

```
log-level = INFO
```
  * Specifies the log verbosity.
  * Possible values: _DEBUG_, _INFO_, _WARNING_, _ERROR_

```
player-encoding = UTF8
```
  * Specifies the character set encoding of the data passed from a player adapter to clients.
  * Possible values: a character set identifier (see output of <tt>iconv -l</tt>)

```
config-version = x.x.y
```
  * Used internally to check configuration compatibility.
  * Do not change this.

# Player Specific Configuration Options #

## MPD ##

```
custom-mpd-host = localhost
```
  * Host running the MPD to interact with.

```
custom-mpd-port = 6600
```
  * Port on the host above to contact the MPD.

```
custom-mpd-music-dir = /var/lib/mpd/music
```
  * Root directory of MPD's music directory.
  * Used for searching cover art files (only works if MPD is at _localhost_).

```
custom-mpd-password =
```
  * Password to use when connecting to MPD.
  * Must be set if you've configured your MPD to restrict certain actions with a password requirement.

## MPlayer ##

```
custom-mplayer-cmdfifo = ~/.cache/remuco/mplayer/cmdfifo
```
  * FIFO file to use to send commands to MPlayer.
  * The file specified here must be set as MPlayer's _input file_: <tt>mplayer -input file=~/.cache/remuco/mplayer/cmdfifo ...</tt>.

```
custom-mplayer-statusfifo = ~/.cache/remuco/mplayer/statusfifo
```
  * FIFO file to use to read output from MPlayer.
  * MPlayer's standard output must be redirected to that file in order to get status updates in clients: <tt>mplayer ... | tee -a ~/.cache/remuco/mplayer/statusfifo</tt>