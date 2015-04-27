The Android client for Remuco is work in progress, but basic features already work. Following you'll find some instructions to build and test the latest Android client from the source.

<h1>Outline</h1>


# Prerequisites #

You will need a few things to compile the Android client.

  * A working Android SDK ≥ 8 with at least one target environment already created (at least one VM). See [the Android SDK docs](http://developer.android.com/sdk/index.html) for details.
  * A few dependencies from your linux distribution:
    * **mercurial** (the soruce control tool used by Remuco)
    * **sun-java6-jdk** (might be on an archive that is not available by default on your distribution, as it's not entirely free software)
    * **ant** ("make" for Java)

# Setup the build environment #

Pull the Remuco source:

```
$ hg clone https://remuco.googlecode.com/hg/ remuco
```

Go in the root directory for the android client:

```
$ cd remuco/client/android
```

You will have to create a file named `local.properties` to tell your compiler where all the Android SDK stuff is located. Thankfully, there is already a file named `local.properties.exemple` wich you can just copy/paste or rename as `local.properties` after you have edited it. If you installed the Android SDK in your home directory, it might look like this:

```
sdk.dir=/home/john/android-sdk-linux_86
```

Change that to suit your needs.

Now you are ready to compile your Android Client and create the _APK_ file you need to install on your phone or to test the client in the emulator.

# Building #

If you run

```
$ ant debug
```

an _APK_ file named `Remuco-debug.apk` (or `Remuco-unsigned.apk`) will be created in the `bin` sub-directory.

# Run the client on a real device #

Transfer the built _APK_ file to your phone, e.g. using a USB connection. On the phone, browse to the location where you copied the _APK_ file to and install it (choose your favorite file explorer).

Your phone will complain about the fact that the application comes from an untrusted source (i.e. not from the Market). In order to install it anyway, you'll have to enable the possibility to install such applications in the phone's settings. The corresponding option is located at _Settings_ → _Applications_ → _Unknown Sources_ (or whatever it is called in your locale).

Once installed, start the Remuco application and choose your favorite connection method, WiFi or Bluetooth. For the first method, you'll have to know your computer's IP address within your local network.

# Run the client in the emulator #

[Please check the official Android SDK docs.](http://developer.android.com/guide/developing/building/building-cmdline.html#RunningOnEmulator)

Once installed on an emulated device, start the Remuco app in the emulated device and connect via WiFi to `10.0.2.2` (this refers to _localhost_ of your machine running the emulator).

# Developer information #

Though the Android Eclipse plugin is a good way to develop for Android, the `client/android` folder should not contain IDE specific files - it should always be possible to build the Android client using the Ant `build.xml` file only.