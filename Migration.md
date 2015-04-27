[Rationale](#Rationale.md)<br />
[Progress](#Progress.md)<br />
[Alternatives](#Alternatives.md)<br />

# Rationale #

The main motivation to move away from SF is that the SF website is to slow and messy to have fun working on and managing Remuco. Especially working with trackers and forums and managing downloads is just a bad experience. SF tried to improve their hosting service in the last month by setting up a new site design and by providing a zoo of hosting tools through the hosted app service. However, the new design lacks fundamental style guidelines (bad colors, over-navigated, to much clicks to get to some point). The hosted apps are good on their own but they totally lack consistency (and everything is so slow .. argh). I really appreciate SF's hosting service for open source projects but nowadays it stands behind [other possibilities](Migration#Alternatives.md).

# Progress #

## Downloads ##

_Migration status:_<font color='#4e9a06'>FINISHED</font>

Then latest release (0.9.1.1) is available [here at GC](http://code.google.com/p/remuco/downloads/list), all other releaser still are [at SourceForge](http://sourceforge.net/projects/remuco/files).

## Tracker and Forum ##

_Migration status:_<font color='#4e9a06'>FINISHED</font>

Forums and trackers at SF have been marked deprecated. Open or interesting closed tracker items as well as active or informative forum threads have been migrated to the [new issue tracker](Issues.md). However, for reference the [old trackers](https://sourceforge.net/tracker/?group_id=166515) and [old forums](https://sourceforge.net/forum/?group_id=166515) at SF are still accessible for some time.
Of course, new issues should be posted here at GC.

## Source Code Management ##

_Migration status:_<font color='#4e9a06'>FINISHED</font>

Finally I've managed to convert Remuco's SVN repository to a Mercurial repository while keeping as much history information as possible. The new Mercurial repository contains all trunk changes ever made in SVN and all tags. Branch history has been discarded .. who cares, I do not. Source is now available here at GC (for quick access and issue integration) _and_ at BitBucket (for collaboration). And just in case you ask .. I have no striking reason why I chose Mercurial and not Git. I'm new to both and I just have to start at some point - which is Mercurial by accident.

## Website ##

_Migration status:_<font color='#4e9a06'>FINISHED</font>

Most content of the previous Remuco website at SF has been migrated to this wiki now. Not everything looks as neat as it was in the MediaWiki before. However, this a thing to fix in small steps whenever there are some 10 minutes to tweak page design. Unfortunately th GC wiki does not allow CSS which means all layout stuff has to be done with tables .. #+/&%§x.

## Project News ##

_Migration status:_<font color='#4e9a06'>FINISHED</font>

Until migration is complete, news are posted in parallel [here](News.md) and at SF.

# Alternatives #

Before deciding to go to GC, I've had a look at some other hosting facilities and the final decision was not easy. I've short-listed Launchpad, GitHub, BitBucket and, of course, GC. The driving main requirement for my selection was to combine as most things as possible at one place (source code, website/wiki, issue tracker, support system and downloads). Here is a short review with pros and cons for each:

Launchpad:
  * + Site design
  * ++ Bug tracker
  * ++ Answers system (as support system)
  * -  No wiki
  * -  Although individual projects are support, everything still feels like being part of a distribution management system
  * -  Focus is on development rather than on a whole project
  * -  Bazaar (seems to be backwards compared to Mercurial and Git)

GitHub:
  * +  Site design
  * ++ Community development
  * +  Wiki
  * +  Space for a static website
  * -  Issue tracker (very basic)
  * -  Focus is on development rather than on a whole project
  * -  No user support system

BitBucket:
  * ++ Site design
  * ++  Community development
  * ++ Wiki
  * +  Issue tracker
  * -  Focus is on development rather than on a whole project
  * -  No user support system

Google Code:
  * ++ Site design
  * ++ Wiki
  * ++ Issue tracker (very flexible)
  * +  Issue tracker can be used as support system
  * +  Google groups can be uses as support system
  * +  Project focused
  * +  Space for a static website (using source code repository)
  * -  Community development not as good as in GitHub or BitBucket
  * -  Even if Google is not evil, one day the evil guys will come to Google ;)

To summarize it was really hard to decide between GitHub, BitBucket and GC. Finally it's GC because it combines most of the required features. However, I'm thinking of managing source code at BitBucket or GitHub. I'm just new to DSCM and I have to figure out my favorite, Mercurial or Git. Switching between Mercurial and Git later should not be a problem.