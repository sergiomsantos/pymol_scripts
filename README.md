# PyMOL utility scripts

### Installation

1. Download the selected script files to your local drive;
2. Add the file to your `.pymolrc` for automatic loading
   whenever a new instance of PyMOL is created.


### Example

The following example automatically loads the `loadr.py` script:

```
# file ~/.pymolrc

run ~/path/to/loadr.py
```

To test, open a new instance of PyMOL and in the command prompt type:

```
PyMOL>help loadr

DESCRIPTION

    "loadr" load remote file.

    "loadr" will attempt to load a remote file from the given host.
    If the host is not provided, the action will fallback to loading
    the file with the given name from the local drive.

USAGE
 
    loadr filename, [host=None [, *args [, **kwargs]]]

    (...)
```