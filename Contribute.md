

# Contribute as a user #

You don't need coding skills to contribute to Remuco. We are also happy if you
  * [report bugs](http://code.google.com/p/remuco/issues/entry?template=Report%20a%20bug),
  * [submit a screenshot](Screenshots#You_have_a_nice_screenshot?.md),
  * use the tool _remuco-report_ to extend the [Remuco client device database](ClientDevices.md) or
  * just say thanks to the developers ;)

# Contribute as a developer #

Remuco is made to support a wide range of media players. However, we cannot afford to write and maintain player adapters for all used players.

**That's the point were we need you:** PlayerAdapterWritingGuide.

You may also be interested in the [list of issues which need contribution](http://code.google.com/p/remuco/issues/list?q=label:NeedsContribution).

General development documentation can be found in the [wiki pages about Remuco development](http://code.google.com/p/remuco/w/list?q=label:Development).

Feel free to [ask for development support](http://groups.google.com/group/remuco) any time.

## Guide Lines ##

These are guide lines, no laws. Be smart :)

#### Coding style ####

  * **Python**: Write [PEP 8](http://www.python.org/dev/peps/pep-0008/) compliant Python code.
  * **Java**: Format your code with the Eclipse built-in Java formatter (if you don't use Eclipse, have a look into existing Java files to get an idea about the code style used in Remuco).

#### Commit messages ####

  * Commit with a user name setting like _John Doe <mail@contact.net>_.
  * Write meaningful commit messages.
  * The first line should be a short (≤ 50 chars) summary of the change and start with the component affected by a change, e.g.: _Banshee: add rating control_
  * Details about the change should come after an empty second line.
  * Details should not be longer than 72 chars.
  * Try to write in present tense (_fix issue X_ instead of _fixed issue X_).
  * More information in this blog post: [A Note About Commit Messages](http://www.tpope.net/node/106).

## Get the source ##

_New to distributed version control systems? Read the [newbie instructions below](#Newbie_help.md)!_

You can choose between the [default Mercurial repository](http://code.google.com/p/remuco/source/checkout):
```
$ hg clone https://remuco.googlecode.com/hg/ remuco.hg
```
the [Mercurial mirror at BitBucket](http://bitbucket.org/obensonne/remuco/overview/):
```
$ hg clone http://bitbucket.org/obensonne/remuco/ remuco.hg
```
or the [Git mirror at GitHub](http://github.com/obensonne/remuco):
```
$ git clone git://github.com/obensonne/remuco.git remuco.git
```

## Share contributions ##

When you feel your changes are ready for a review or for integration into Remuco, push them to a publicly available repository:

  1. [Clone here at Google Code](http://code.google.com/p/remuco/source/clones)
  1. [Fork at BitBucket](http://bitbucket.org/obensonne/remuco/) _(recommended)_
  1. [Fork at GitHub](http://github.com/obensonne/remuco)

To let the Remuco developers know you have some changes, post a note to the [mailing list](http://groups.google.com/group/remuco).

## Newbie help ##

If you are new to distributed version control systems, here are some instructions to get you started.

We are going to use Mercurial for version control and BitBucket to share contributions

#### Set up a collaborative working environment ####

  1. If not done yet, [create an account at BitBucket](http://bitbucket.org/account/signup/).
  1. Log in to your BitBucket account and fork the [Remuco repository](http://bitbucket.org/obensonne/remuco/) by hitting _fork_ at the top.
  1. Now you have a fork of the Remuco repository you can start working on.
  1. If not done yet, install Mercurial on your system.
  1. Make a local clone of _your_ Remuco repository (assuming your user name is _johndoe_):

```
$ hg clone https://johndoe@bitbucket.org/johndoe/remuco/
```

#### Do some changes to the Remuco code ####

You can now start to work on Remuco, doing some changes to the code. Commit your changes often:
```
 $ hack .. hack .. hack
 $ hg add <new-files>
 $ hg commit
```

These are _local_ commits, no changes leave your work station yet. Besides that, basic version control commands (commit, add, remove, revert) are quite similar to SVN.

When writing code and commit messages **please** follow the [guide lines above](#Guide_Lines.md).

If you accidentally committed a bad change or bad commit message, you can undo _the last_ commit by running
```
 $ hg rollback
```

From time to time you should ensure your fork is in sync with the Remuco mainline by doing
```
 $ hg pull -u https://johndoe@bitbucket.org/obensonne/remuco/
```
Sometimes you have to do a merge then:
```
 $ hg merge
 $ hg ci -m "Merge in changes from mainline"
```
Here you may want to read the [Mercurial guide on merging changes](http://hgbook.red-bean.com/read/a-tour-of-mercurial-merging-work.html).

#### Make your changes public ####

When you feel your changes are ready for a review or for integration into Remuco, push them up to your public fork:
```
 $ hg push
```
Now your changes _leave_ your local work station but they are not yet part of the main Remuco repository - everything is still in _your fork_.

If you want your changes to get into the main repository, drop a note on the [mailing list](http://groups.google.com/group/remuco) to inform the developers about your contributions.

#### Further information ####

I really recommend to spend some 2 hours with reading the [Mercurial Guide](http://hgbook.red-bean.com/) - I'm sure you'll not regret it!

However, if you are in a hurry, BitBucket's [getting started information](http://bitbucket.org/help/UsingBitbucket) may be a better choice to start.

Feel free to [ask for support](http://groups.google.com/group/remuco) if needed.