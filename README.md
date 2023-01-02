# Random Vid

Simple script that generates and plays a randomly ordered playlist in VLC from a provided path. You must have VLC installed, and you must be able to call `vlc` from the command line to launch it.

## Usage/Examples

Run the program:
`python3 random_vid.py <path>`

Limit the size of the paylist to 10 videos:
`python3 random_vid.py <path> --limit 10`

By default, the program will recursively look into all subdirectories for files. To only look at the provided path:
`python3 random_vid.py <path> --no-recursive`

See the help menu for all options:
`python3 random_vid.py --help`

## Why not use the python-vlc library?

This script does not use the python vlc library as launching videos using this library disables much the controls in the VLC GUI, and I still want access to these controls through the GUI. This tool is simply intended to be a shortcut for launching a random playlist.
