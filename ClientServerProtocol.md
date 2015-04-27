<h1>Overview</h1>


Remuco uses socket based stream connections for client server communication. Sockets are either Bluetooth or Inet (WiFi) based.

Communication between client and server is message based. The following section describes the message exchange during the life cycle of a client server connection. Messages are described in detail in section [Messages](#Messages.md). Binary representation of message payload data is described in section [Binary Data](#Binary_Data.md).

# Message Exchange #

<table>
<tr valign='top'>
<td>

The sequence diagram illustrates the message exchange between <b>Client</b> and <b>Server</b>. <b>Adapter</b> represents a specific player adapter. Communication between server and adapter is not part of the client server protocol and is only listed to illustrate the context of messages transferred between client and server.<br>
<br>
<h2>Connection Setup <code>[1]</code></h2>

<ul><li>Once a socket based stream connection has been set up between client and server, the server sends a <tt>[[#Structure|HELLO]]</tt> message to the client.<br>
</li><li>Subsequent the client sends a <tt>CONN_CINFO</tt> message which contains some information about the client.<br>
</li><li>The server replies with<br>
<ul><li>a <tt>CONN_PINFO</tt> message which contains information about the media player,<br>
</li><li>a <tt>SYNC_STATE</tt> message which contains information about the media player state (playback, volume, ...),<br>
</li><li>a <tt>SYNC_PROGRESS</tt> message which contains information about the progress of the currently played item and<br>
</li><li>a <tt>SYNC_ITEM</tt> message which contains information about the currently played item (meta data, cover art).</li></ul></li></ul>

At this point a connection between client and server is established. Now sync <code>[3]</code>, control <code>[2]</code>, request <code>[4]</code> and action <code>[5]</code> messages may be exchanged repeatedly until the connections gets shut down <code>[6]</code>.<br>
<br>
<h2>Control <code>[2]</code></h2>

TODO<br>
<br>
<h2>Synchronization <code>[3]</code></h2>

TODO<br>
<br>
<h2>Requests <code>[4]</code></h2>

TODO<br>
<br>
<h2>Actions <code>[5]</code></h2>

TODO<br>
<br>
<h2>Connection shutdown <code>[6]</code></h2>

TODO<br>
</td>
<td>
<img src='http://wiki.remuco.googlecode.com/hg/images/client-server-protocol.png' />
</td>
</tr>
</table>

# Messages #

## Structure ##

Each message consists of 2 byte message ID, 4 byte message paylod size and a variable number of bytes payload data:

| **Byte** | 0 | 1 | 2 | 3 | 4 | 5 | ... |
|:---------|:--|:--|:--|:--|:--|:--|:----|
| **Content** | ID | ID | SIZE | SIZE | SIZE | SIZE | PAYLOAD |

Endian of multibyte numeric values is _net order_ (big endian).

One exception of this structure is the <tt>HELLO</tt> message sent from the server to a client at the beginning of the connection setup:

| **Byte** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---------|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| **Content** | <tt>0xFF</tt> | <tt>0xFF</tt> | <tt>0xFF</tt> | <tt>0xFF</tt> | <tt>0x08</tt> | <tt>0xFE</tt> | <tt>0xFE</tt> | <tt>0xFE</tt> | <tt>0xFE</tt> |

This message is used to check protocol compatibility between client and server. <tt>0x08</tt> specifies the protocol version.

## IDs ##

Message IDs are defined here: <tt><a href='http://code.google.com/p/remuco/source/browse/base/module/remuco/message.py'>base/module/remuco/message.py</a></tt>

## Parameters ##

Messages may have parameters (payload). Possible parameters are the objects defined at <tt><a href='http://code.google.com/p/remuco/source/browse/base/module/remuco/data.py'>base/module/remuco/data.py</a></tt>. The purpose of these objects is to pack a set of basic data elements (integer, string, ...).

For each parameter object in <tt>data.py</tt> the basic data elements are those which get set with <tt>set_data()</tt> and which are returned by <tt>get_data()</tt>. The types of the basic data elements are specified by the return value of the method  <tt>get_fmt()</tt>.

For messages from client to server, the method <tt>PlayerAdapter.handle_message()</tt> in <tt><a href='http://code.google.com/p/remuco/source/browse/base/module/remuco/adapter.py'>base/module/remuco/adapter.py</a></tt> gives information about the mapping message ID ↔ message parameter.

For messages from server to client, browsing the server code for calls to the function <tt>build_message()</tt> in <tt><a href='http://code.google.com/p/remuco/source/browse/base/module/remuco/net.py'>base/module/remuco/net.py</a></tt> gives information about the mapping message ID ↔ message parameter.

On client side similar information can be found in all classes which implement the interface <tt><a href='http://code.google.com/p/remuco/source/browse/client/common/src/remuco/client/common/serial/ISerializable.java'>ISerializable</a></tt>.

### Example ###

The message payload object <tt>Progress</tt> contains the current progress and duration of an item (song, video, ..). It is the parameter of the message <tt>SYNC_PROGRESS</tt>.

```
class Progress(serial.Serializable):
    """ Parameter of the sync progress message (message.SYNC_PROGRESS) sent to
    clients.
    
    """
    def __init__(self):
        
        self.progress = 0
        self.length = 0
        
    def __str__(self):
        return "(%d/%d)" % (self.progress, self.length)
        
    # === serial interface ===
        
    def get_fmt(self):
        return (serial.TYPE_I, serial.TYPE_I)
        
    def get_data(self):
        return (self.progress, self.length)
```

As this message only gets send to clients (and not vice versa), there is no <tt>set_data()</tt> method here - it only needs to get serialized for outgoing messages to clients. Deserialization is not necessary here.

The method <tt>get_fmt()</tt> returns the types of the basic data elements, two integer in this case.

The method <tt>get_data()</tt> returns the basic data elements according to the format vector from <tt>get_fmt()</tt>. In this case it returns two integers, the progress of the current item and its duration (both in seconds).

# Binary Data #

This section describes the binary representation of basic data types (integer, string, arrays, ..) in the Remuco client server protocol.

## Code examples ##

  * Server-side (de)serialization of basic data types in Python:
    * <tt><a href='http://code.google.com/p/remuco/source/browse/base/module/remuco/serial.py'>base/remuco/serial.py</a></tt>
  * Client-side (de)serialization of basic data types in Java:
    * <tt><a href='http://code.google.com/p/remuco/source/browse/client/common/src/remuco/client/common/serial/Serial.java'>client/common/src/remuco/client/common/serial/Serial.java</a></tt>
    * <tt><a href='http://code.google.com/p/remuco/source/browse/client/common/src/remuco/client/common/serial/BaIn.java'>client/common/src/remuco/client/common/serial/BaIn.java</a></tt>
    * <tt><a href='http://code.google.com/p/remuco/source/browse/client/common/src/remuco/client/common/serial/BaOut.java'>client/common/src/remuco/client/common/serial/BaOut.java</a></tt>