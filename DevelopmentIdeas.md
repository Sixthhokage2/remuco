<h1>Overview</h1>

This page presents and discusses some ideas where to go with Remuco in the future. It is not intended for specific features but for general design issues.



# Types of application to support #

Initially Remuco has been designed to control audio players. Meanwhile it also works with video (or audio+video) players and there even is an adapter for a presenter app (Okular). However, the non-audio support can be seen as limited patch-work. I think in the future the type of an application should be better integrated in the adapter API and in the client interface. Independent of this, how broad should the scope of Remuco be? Should it be possible to write adapters for shell terminals or desktop control? Should we strictly stick to audio players?

## Comments ##

**Oben:** I would vote for staying with _media_ applications, i.e. anything which shows or plays some kind of media (presenters, photo slide show apps, audio players, video players).

**Pawel:** I think that Remuco should be focused on media apps - to control terminals or desktop it will be necessary to completely change client and server. I have also some doubts abut media center applications and these applications have completely another way of control than normal media players. To fully control media center we must navigate trough many levels of menus so normal player control mode is useless. In that case we should have two modes: navigation mode and player control mode that is activated when we choose what we want to do from menu.

**Oben:** I think providing a navigation mode is not that difficult. It is even required for media apps playing DVDs. So in case we set the scope to media players (not only audio), a navigation mode is a requirement. Technically it's not more than supporting _up_, _down_, _left_, _right_ and _select_ commands. That should catch most DVD menu and media center use cases. Correct me if I'm wrong.

**Igor:** I think web browsers qualify as "anything which shows some kind of media", but adapters to control firefox seem a bit of a stretch. "Anything with slides (photos, presentations), video or audio" sounds less... chaotic.

**Oben:** Agree.

# Flexible client interface configuration #

This somehow depends on the scope of Remuco discussed above. Also see [issue 69](https://code.google.com/p/remuco/issues/detail?id=69), the initial trigger for the discussion in this section.

Currently player adapters can specify which player information they have access to (e.g. repeat status, volume, ...). This influences what is shown in the client interface. For audio players, this works well. For video players and presenter apps like Okular, this is not sufficient. Especially for video players, the interface may change, e.g. when a DVD navigation menu is active. What would be the most flexible (but still KISS) approach for adapters to influence the client interface, i.e. what is shown at and what can be controlled by clients.

In general these 2 extremes are possible:
  1. Adapters precisely specify what elements are shown where on clients and which keys map to which remote function.
    * Great flexibility.
    * Blows up player adapters.
  1. Adapters can specify a type of interface, e.g. _audio_, _video_, _navigation_, _presenter_, ...
    * Does not consider specific features (rating, repeat, ...)

Of course something in between would be best here.

## Comments ##

**Pawel:** Comment to that point is in previous section.

**Igor:**  The navigation mode seems the way to go for now. It would instantly enable us to control more of the media player and sounds simple enough to add to current adapters. How about adding some kind of tabbed interface in the client? Imagine the user could choose between these "tabs" (or "interfaces", but really it's just a naming issue):
  * Navigation, where North-East-West-South map directly to 8-6-4-2, Select maps to 5, pageup/down could be there too, etc. All of this can be changed like we do today.
  * Control, the standard play/pause/fast forward/rewind (for audio/video), first/last/next/previous slide or something like that
  * Meta, for rating, subtitle and audio track selection (specific for DVD sessions), access playlists, etc.
In the client, to tell the interfaces apart could be as simple as three squares on the corner, with one of them highlighted, or we can complicate matters a bit by adding different screens, say, Navigation shows a compass rose and just the name of the media currently played, whereas Control would be the way main client screen is today, and Meta would be more of a listing.
I think this addresses both extremes, since CONN\_PINFO would still carry the adapters' "orders" for the client to follow, but this more abstract interface allows the client to specialize when facing different use cases.
The main point in this is that we are, indeed, overloading the keys, which can be bad, but only if the user cannot see that he's switched context.

**Oben:** I like the idea of having 3 screen modes (interfaces, tabs, ...). _Control_, _navigation_ and _meta_ seems reasonable. I would still put the rating on the _control_ screen as this is - at least in my use case - a very often used feature which should not require an interface switch. A _navigation_ interface would be straight forward. In contrast, the design and functionality of the _meta_ screen needs some more brainstorming.

As we seem to have agreed where to go roughly, we should discuss further details either on the mailing list or in the issue tracker.

# DBus for server - player adapter interaction #

Currently player adapters must be written in Python. They import the Python module _remuco_ which implements the Remuco server functionality. Another approach would be to make server and adapters different processes which communicate with each other using DBus.

## Advantages ##

  * Player adapters may be written in any language (which has DBus bindings).
    * Though Python is a great language and well supported among media player applications, it does not catch them all. For instance the Banshee adapter ideally would be written as a Banshee plugin in C#.
  * There only need to be _one_ server process which manages _multiple_ player adapters.
    * Clients don't need to disconnect to switch between players.
    * Clients can connect to the server instance and start and stop players (and adapters) remotely.
    * For WiFi connections the port number does not need to get adjusted when using Remuco for multiple players simultaneously.

## Disadvantages ##

  * In the current Python-only approach it is easier to write player adapters (most ugly things are hidden within the _remuco_ module).
    * Constants and utility functions implicitely are available in adapters via the _remuco_ module.
    * Capabilities can be detected automatically (to some extend) by testing which methods actually have been overridden.
  * DBus communication is one more possible error source to manage.
  * Debugging gets more complicated (multiple processes and log files).
  * Makes it hard to port Remuco to non-Linux system, for instance Windows: http://github.com/cpatulea/remuco _(updated 9 Feb 2010)_

## Comments ##

**Oben:** The big advantage I see in splitting server and adapters into different processes is that I could start a player from the phone.

**Igor:** For audio players this is cool. I wouldn't use it to start a video player, though. It would be a pain to navigate the filesystem just to find a movie file.
What if you could spawn adapter-specific servers? If necessary, there could be a central, DBus-capable server, and then Banshee's adapter would be in C#. But if I wanted, I could start a standard python-based adapter, which in turn would have its own instance of a server, but in a "sandboxed" temporary fashion. Make sense? :P

**Oben:** Er .. partly. Do you really mean having 2 Banshee adapters, one in C# and one in Python?

**Igor:** In a way, yes. But just because we already have a banshee adapter. My point is making remuco able to work in both worlds (directly through python objects/inheritance and d-bus messages). That way, banshee's C# adapter would interface with the central "remuco d-bus server", just as any other adapter using d-bus; but also being able to spawn a somewhat castrated server+adapter the way we do today (i'm thinking MASTER\_MODE in remuco-mplayer), concurrently and even different adapters.
This is bad because code may blow up, and it is bad because we might run into problems when multiple sandboxed servers try to access bluetooth hardware, and it is also bad because we add an extra layer of complexity, but on the other hand we gain the flexibility to control independent of where the adapter is... if that's any good.