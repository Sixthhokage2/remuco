## Quick Start ##

To develop a player adapter, use _[fooplay](http://code.google.com/p/remuco/source/browse/#hg/adapter/fooplay)_ as a template and implement it as
described in the file _[api.html](http://remuco.googlecode.com/hg/doc/api.html)_.

To test the _fooplay_ adapter, simply run it as a Python script. It requires the
Python module _remuco_ which is available if you installed another player
adapter before. Otherwise, just add <tt>path-to-remuco/base/module</tt> to _PYTHONPATH_
before running the _fooplay_ adapter. For instance
```bsh

$ export PYTHONPATH=path-to-remuco/base/module:$PYTHONPATH
$ path-to-remuco/adapter/fooplay/remuco-fooplay
...```

starts the _fooplay_ adapter without installing anything. Try it, it's easy :)

Once the adapter is running, you can easily test client interaction by running the client in an emulator as described at ClientCustomization.

## Support ##

If you need help, just [ask for it](http://groups.google.com/group/remuco).

## Get your changes into Remuco ##

See [the workflow section in the Contribute page](http://code.google.com/p/remuco/wiki/Contribute#Recommended_workflow).