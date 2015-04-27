

## Can I use Remuco for multiple players simultaneously? ##

For sure. This works out of the box using Bluetooth connections.

For WiFi connections you have to tweak [player adapter configurations](GettingStarted#Configuration.md) so that each adapter uses a unique port. Here is an example which sets distinct ports for Banshee and VLC in <tt>~/.config/remuco/remuco.cfg</tt>:

```
...
[Banshee]
wifi-port 40001
...
[VLC]
wifi-port 40002
...
```

_Note: Remuco ≤ 0.9.2 had a slightly different configuration system. See PlayerAdapterConfiguration in case you are using an older Remuco version._

On the client, create a new WiFi connection for each player and set the port as configured.

## Bluetooth problems ##

### Device scan fails ###

First, check if the Bluetooth device on your computers is in _inquiry_ mode, i.e. it must be discoverable. You can check this with:
```
 $ hciconfig
```
In the output must be a line like this:
```
 UP RUNNING PSCAN ISCAN
```
If this is not the case, you can enable _inquiry_ mode with:
```
 $ hciconfig hciX piscan
```
where _X_ is the number of the Bluetooth device to configure (0 for the first). If available, you may also use your graphical tool of choice for setting your Bluetooth dongle _visible_ and _conncetable_.

If this does not help, you can set your system's Bluetooth address manually in the client when creating a new Bluetooth connection - this circumvents the need for a device scan.

### Service search fails ###

<table><tr>
<td>
First, when a player adapter is running, check if the Remuco Bluetooth service is active:<br>
<pre><code> $ sdptool browse local<br>
</code></pre>
Among others this should list an entry for each running player adapter. Here is an example when using Rhythmbox:<br>
<br>
<pre><code>Service Name: Rhythmbox<br>
Service RecHandle: 0x10007<br>
Service Class ID List:<br>
  UUID 128: 025fe2ae-0762-4bed-90f2-d8d778f020fe<br>
  "Serial Port" (0x1101)<br>
Protocol Descriptor List:<br>
  "L2CAP" (0x0100)<br>
  "RFCOMM" (0x0003)<br>
    Channel: 1<br>
Profile Descriptor List:<br>
  "Serial Port" (0x1101)<br>
    Version: 0x0100<br>
</code></pre>

Some devices fail with the standard service/channel search. On the client you can edit Bluetooth connections to try alternative service/channel search strategies. Try a <i>failsafe</i> search! If even this does not help, try to manually set the channel of the service to connect to (in the example above it is <i>1</i>) in the Bluetooth connection editor screen (see image on the right).<br>
<br>
Based on user feedback you have to manually set the channel on <i>Blackberry</i> devices. Server and client must use a channel ≥ 7! See the <a href='GettingStarted#Configuration.md'>player adapter configuration instructions</a> for how to set a fixed Bluetooth channel on the server side.<br>
</td>
<td>
<img src='http://wiki.remuco.googlecode.com/hg/images/exos/emulator-bluetooth-screen.png' />
</td>
</tr></table>

### I'm still lost ... ###

Finally it is always a good idea to test Remuco on another computer or with another mobile device or both. Bluetooth problems mostly are caused by the Bluetooth stack on the computer or on the mobile device. Using Remuco in another environment helps to detect where the problem originates.

If all this does not help [check if your specific problem is a known one](http://code.google.com/p/remuco/issues/list?can=1&q=label%3ABluetooth).

## Timeout while waiting for Hello message ##

This may have several reasons, however, some users with Bluetooth devices reported that this could be fixed by setting a fixed Bluetooth channel number (preferably not 1). See the section _Service search fails_ above.

## Incompatible client and server versions ##

The reason is probably because you installed a distribution specific package of Remuco and the distribution package has been updated but you did not install the corresponding new client on your device yet.

You find the server version at the beginning of a player adapter's log file, for instance <tt>~/.cache/remuco/xmms2/log</tt>.

You can check the client version by issuing the _System_ command in the client's _Log_ screen.

## What's that report tool for? ##

The tool _remuco-report_ makes it easy for users to contribute to the [list of Remuco compatible devices](ClientDevices.md). It sends information about seen client devices to <tt><a href='http://remuco.sourceforge.net/cgi-bin/report'>http://remuco.sourceforge.net/cgi-bin/report</a></tt>.

Before this tool submits any data, you get a chance to review the data to report.

## How can I control the master volume? ##

The [Remuco configuration file](GettingStarted#Configuration.md) has some options to enable and configure master volume control instead of controlling a player's volume.

_The information below is only relevant for Remuco ≤ 0.9.2._

If you prefer to control your system's master volume instead of a player's volume level, put a script called <tt>volume</tt> into the configuration directory of the corresponding player adapter, e.g. into <tt>~/.config/remuco/banshee/</tt>. Alternatively, to use the master volume for all player adapters, put this script into <tt>~/.config/remuco/</tt>

The volume script must behave as follows.
  * Given no argument, it must print out the volume in percent.
  * Given argument _up_, it must increase volume by some percent (5 is good value).
  * Given argument _down_, it must decrease volume by some percent (5 is good value).
  * Given argument _mute_, it must mute volume.

An example script can be found in the documentation directory of the Remuco package. This script uses the tool _amixer_. In most cases it should work out of the box. Otherwise just have a look into it for how to adjust it for your system.

Make sure the script is executable!

## I have another question ... ##

Have you read the [known issues](GettingStarted#Known_Issues.md)? Please also check [existing support tickets](http://code.google.com/p/remuco/issues/list?can=1&q=type=Support)? If you don't find an answer there, [ask a new question](http://code.google.com/p/remuco/issues/entry?template=Get%20usage%20support).