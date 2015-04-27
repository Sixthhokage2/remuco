#### Get the latest source code ####

```
 $ hg clone https://remuco.googlecode.com/hg/ remuco-hg
 $ cd remuco-hg
```

Or if you've done that before already, update your clone:
```
 $ hg pull -u
```

#### Player Adapters ####

_Remove any distribution packages of Remuco first!_

Installing player adapters works exactly like described in GettingStarted:

```
 $ sudo make install-PLAYER
```

Script-based player adapters can also be started right from the source without installation:

```
 $ PYTHONPATH=base/module:$PYTHONPATH adapter/fooplay/remuco-fooplay
```


#### MIDP Client ####

This is the original JavaME client.

Build the client:
```
 $ cd client/midp
 $ ./setup.sh # automatically download required tools and set up the build environment
 $ ant dist # build the client
```

_Details on these commands can be found at [MIDP](MIDP.md)._

After a successful build the client files are located in the sub-directory <tt>app/</tt> and ready to install on your phone. Further client installation information can be found at GettingStarted.

#### Android Client ####

We have an experimental Android client. For more information see [Android](Android.md).