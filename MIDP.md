This page contains instructions on how to build the MIDP client from source and how to customize for specific phones or features.

<h1>Outline</h1>


# Good reasons for client customization #
  * The default client does not work on your device (e.g. Windows Mobile device).
  * You want to change the client's application logo size.
  * You need to reduce the size of the ''JAR'' file.
  * You have a connection permission problem (''Not allowed to connect'').
  * You are interested in client development and need some start-up aid.

# Preparation #

## Download ##

If not done already, download and extract the latest Remuco package to a place of your choice, referenced below as <tt>path/to</tt> (things work similar if you prefer to [checkout source from the repository](BleedingEdge.md)).

On a command line, switch into the directory <tt>client</tt> within the extracted Remuco package:

```
 $ cd path/to/remuco-x.y.z/client/midp
```

## Configure build environment ##

To build the client [Ant](http://ant.apache.org/) ≥ 1.7 (incl. optional tasks) is required. Run
```
 $ ant -version
```
to check if and which version of Ant is available on your system.

Additionally the tools [ProGuard](http://proguard.sourceforge.net/) ≥ 4.2 and [MicroEmu](http://www.microemu.org/) ≥ 2.0.3 are needed. Here the script <tt>setup.sh</tt> is your friend. Running
```
 $ ./setup.sh
```
downloads _MicroEmu_ and _ProGuard_, extracts it into the directory <tt>tools/</tt> and sets up the file <tt>build.properties</tt> accordingly. If you do not want to or cannot use this script, download the tools manually and create and edit <tt>build.properties</tt> based on <tt>build.properties.example</tt>.

## Check build environment ##

Running
```
 $ ant -p
```
gives you a list of targets to call with _Ant_ (not all targets work out of the box, because some require further adjustments in <tt>build.properties</tt>).

Let's check _MicroEmu_ and _ProGuard_ setup by building a client binary:
```
 $ ant dist
```
This should create a client binary in the directory <tt>app/</tt> - otherwise some error output hopefully helps you to fix your setup.

The built client binary is ready to install on a phone, however, such a binary is already included in the Remuco package. See the next section for typical client customizations.

# Customization #

## Disable optimizations ##

Some phones may have problems with the default, optimized client binary. To disable optimizations, open the file <tt>build.properties</tt> and set the option _dist.proguard.optimize_ to _no_:

```
# =============================================================================
# Configurations for targets 'dist'
# =============================================================================

...

# Whether to optimize and obfuscate the byte code when using !ProGuard.
dist.proguard.optimize=no
#dist.proguard.optimize=yes
```

## Adjust application logo size ##

Per default the logo of the Remuco client is very small (12 pixels only). Most devices accept bigger logo images. To use a bigger logo, open the file <tt>build.properties</tt> and adjust the option _logo.size_:

```
# =============================================================================
# Theme things
# =============================================================================

...

# Size of the application logo.
# Possible values: 12, 16, 24, 32, 48
logo.size=12
```

## Adjust permission settings ##

On some devices, it may be necessary that the client declares which connection permission it requires ([more on this](JavaMeApiPermissions.md)). Permissions are declared in the client's descriptor file. To enable such a declaration, open the file <tt>build.xml</tt> and go to the target _manifest_. There you should see something like this:

```
<!--
<attribute name="MIDlet-Permissions"
           value="javax.microedition.io.Connector.socket" />
<attribute name="MIDlet-Permissions"
           value="javax.microedition.io.Connector.bluetooth.client" />
-->
```

For WiFi, move the first _attribute_ element out of the comment block, for Bluetooth, move the second one.

## Reduce the JAR file size ##

Some devices have a size limit for application JAR files. You can reduce the JAR size by removing some themes or list icon sizes (theme and icon files make more than 90% of the JAR size).

Open the file <tt>build.properties</tt> and adjust the options _theme.list_ and _theme.lics_. For instance, to only use the themes _Emo_ and _Vico_ and to only use list icons of size 16, set the options as follows:

```
# =============================================================================
# Theme things
# =============================================================================

# Adjust if you want to add or exclude themes.
theme.list=Vico,Emo

# If you know the recommended list icon size for your device, you can reduce
# the JAR file size by adjusting this list to only include the next smallest
# icon size.
theme.lics=16
```

# Building #

After you made some customizations, build a new client with:
```
 $ ant dist
```
You'll find the result in the directory <tt>app/</tt>.

# Emulation #

If you configured the build environment as described [above](#Preparation.md) you can test the client in the MicroEmu Emulator, run:
```bsh
 $ ant run.microemu.default```
If you have [Sun's WTK](http://java.sun.com/products/sjwtoolkit/) installed, you may emulate the client in the WTK emulator too:
```bsh
 $ ant run.wtk.default```
Note that there are special configuration options for emulation in <tt>build.properties</tt> !

To connect to a player adapter runing on your computer create a WiFi connection to _localhost_:

<a href='http://wiki.remuco.googlecode.com/hg/images/exos/emulator-add-wifi-connection.png' title='Setting up a WiFi connection to localhost'>
<img src='http://wiki.remuco.googlecode.com/hg/images/exos/emulator-add-wifi-connection.png' height='200' />
</a>
<a href='http://wiki.remuco.googlecode.com/hg/images/exos/emulator-welcome.png'>
<img src='http://wiki.remuco.googlecode.com/hg/images/exos/emulator-welcome.png' height='200' title='Selecting the created connection to connect to a locally running player (adapter)' />
</a>