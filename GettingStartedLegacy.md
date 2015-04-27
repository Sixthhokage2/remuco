<font color='red'>
<i><b>For documentation related to the most recent Remuco release, go to GettingStarted!</b></i>
</font>


---

<h1>Remuco 0.9.2</h1>

---





---


# Installation #

First, install a player adapter on your computer<br />
Second, install the client on your mobile device

_Note:_ You may also be interested in [Remuco packages available for your distribution](DistributionPackages.md).

## Player adapter ##

[Download](http://code.google.com/p/remuco/downloads/list) and extract the latest Remuco release to a place of your choice.

On a command line, switch into the directory where you extracted the Remuco package:
```
 $ cd path/to/remuco-x.y.z
```
Running
```
 $ make help
```
tells you what to do next.
Usually it's as simple as running
```
 $ sudo make install-PLAYER
```
to install the player adapter for _PLAYER_.

After installation there are some files called <tt>install-<code>*</code>.log</tt>. They are needed if you want to uninstall Remuco later.

## Client ##

The client requires a phone with JavaME support (MIDP ≥ 2.0, CLDC ≥ 1.1). If you use Bluetooth to connect to a player adapter, additionally JSR-82 (Java Bluetooth) must be supported. You can check these requirements at the [FPC Bench Result Dababase](http://www.dpsoftware.org/filter.php).

Additionally there is a [list of devices successfully used with Remuco](ClientDevices.md). Once Remuco is running on your system, please help to extend this list by running the tool _remuco-report_.

The client application consists of 2 files:
  * **remuco.jar**
    * the client application to install on your mobile
  * **remuco.jad**
    * a descriptor file which is needed additionally by some phones for installation

The files are located in <tt>client/app/</tt> (if you installed using [distribution packages](DistributionPackages.md) they probably are at <tt>/usr/share/remuco/client/</tt>).

The concrete steps to install the client depend on your phone. Usually it's as simple as sending the _JAR_ file per Bluetooth to your phone or as copying it on your phone and selecting it with the phone's file browser.


---


# Usage #

## Amarok, Audacious, Banshee, Songbird, VLC ##

The player adapter can be started with:
```
$ remuco-PLAYER
```
Replace _PLAYER_ with a correct player name.

A good choice is to set up <tt>remuco-<i>PLAYER</i></tt> as a startup application when you log in to your desktop session.
When the player is not running then the adapter is in sleep mode and won't eat much resources.

**Special note for the _VLC_ adapter:**
Remuco requires DBus control in VLC enabled. This can be configured in VLC at _Tools_ → _Preferences_ ([screenshot](http://wiki.remuco.googlecode.com/hg/images/exos/vlc-preferences.png)).

**Special note for the _Songbird_ adapter:**
The [Songbird MPRIS Add-on](http://addons.songbirdnest.com/addon/1626) needs to be installed.

## Exaile, Rhythmbox, Totem ##

The player adapter actually is a plugin of the player. Thus it gets started automatically once you activate the Remuco plugin within the player.

## MPD ##

The player adapter can be started with:
```
 $ remuco-mpd
```
A good choice is to set up <tt>remuco-<i>PLAYER</i></tt> as a startup application when you log in to your desktop session or when MPD itself get's started. It mainly depends on your MPD setup.

If the player adapter is not running on the same computer as MPD have a look into the MPD section at PlayerAdapterConfiguration.

## MPlayer ##

Add a line to your <tt>~/.mplayer/config</tt> file, telling mplayer to read from the <tt>cmdfifo</tt> file located in the <tt>.cache/remuco/mplayer</tt> folder. Don't forget to change <tt><your user name></tt> to your actual user name.
```
$ echo 'input=file=/home/<your user name>/.cache/remuco/mplayer/cmdfifo' >> ~/.mplayer/config
```
This will allow you to control mplayer from the client, and should be done only once.

Start the adapter (as of now, you need to run the adapter before you run mplayer, and re-run it if mplayer quits):
```
$ remuco-mplayer
```

To be able to read from mplayer, you need to pipe its output to a location known to remuco (set this in ~/.conf/remuco/mplayer/conf):
```
$ mplayer mymovie.avi | tee /home/<your user name>/.cache/remuco/mplayer/statusfifo
```

This should be all, you can now start the client.
But note that you'll need to type that last command everytime you want to play something.

You can add this script to your <tt>~/bin</tt> directory:
```
#!/bin/bash
if [ -z $1 ]; then
        echo "Usage:"
        echo "$0 file2 file2 ..."
        exit 1
fi

teefile=/home/<your user name>/.cache/remuco/mplayer/statusfifo

# if mplayer is installed elsewhere, change /usr/bin/mplayer to the correct location
/usr/bin/mplayer $@ | tee $teefile

```
Name this script <tt>~/bin/mplayer</tt> and make sure <tt>~/bin</tt> precedes <tt>/usr/bin</tt> in your PATH environment variable.


## TVtime ##

The player adapter can be started with:
```
 $ remuco-tvtime
```

For navigating in TVtime's menu with the Remuco client, the keys on the client have special functions when using the TVtime adapter:
| **Client key** | Toggle playing | Toggle repeat | Toggle shuffle | Play previous | Play next | Volume down | Volume up |
|:---------------|:---------------|:--------------|:---------------|:--------------|:----------|:------------|:----------|
| **TVtime key** | _MENU ENTER_ | _SHOW MENU_ | _SHOW MENU_ | _UP_ | _DOWN_ | _LEFT_ | _RIGHT_ |

## XMMS2 ##

The player adapter can be started with:

```
 $ remuco-xmms2
```

To let it start automatically when XMMS2 starts, create a symlink in the XMMS2 user startup script directory:

```bsh
  $ ln -s `which remuco-xmms2` ~/.config/xmms2/startup.d/remuco-xmms2```

## Client ##

Using the client should be quite obvious -- just start it and hit the buttons ;).


---


# Configuration #

Once a player adapter has been started the first time, a configuration file <tt>~/.config/remuco/PLAYER/conf</tt> is created - see PlayerAdapterConfiguration for more information.


---


# Known Issues and Troubleshooting #

If you experience issues, you should use the most recent version or Remuco ;). See GettingStarted.