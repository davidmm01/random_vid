# Random Vid

Simple script that generates and plays a randomly ordered playlist in a media player from a provided path. Default is VLC.

The desired media player must be installed, and must be able to play/queue up videos by a command line invocation following the pattern `<program name> <vid1> <vid2>`.

## Python Dependencies

None! This script only uses python built-ins.

## Usage/Examples

Run the program:
`python3 random_vid.py <path>`

Limit the size of the paylist to 10 videos (default is no limit):
`python3 random_vid.py <path> --limit 10`

By default, the program will recursively look into all subdirectories for files. To only look at the provided path:
`python3 random_vid.py <path> --no-recursive`

Provide a regex to only capture matching videos (default shown):
`python3 random_vid.py <path> --regex ^.*(.mp4)|(.mkv)$`

Provide the command to launch the desired media player (default shown):
`python3 random_vid.p <path> --launch-command vlc`

Perform a dry run that will not launch any programs, instead printing the the generated playlist:
`python3 random_vid.p <path> --dry-run`

Note that all options work with each other. See the help menu for more:
`python3 random_vid.py --help`

## Why not use the python-vlc library?

This script does not use the python vlc library as launching videos using this library disables much the controls in the VLC GUI, and I still want access to these controls through the GUI. This tool is simply intended to be a shortcut for launching a random playlist.
