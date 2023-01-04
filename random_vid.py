import argparse
import os
import random
import re
import subprocess


def check_positive(value):
    """Helper method for argparse type that allows positive integers only."""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Random Vid",
        description="Creates a randomly ordered playlist that is played by VLC",
    )
    parser.add_argument("path", help="source path for the playlist")
    parser.add_argument(
        "--recursive",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="consider any videos that are in subdirectories of the provided path",
    )
    parser.add_argument(
        "--limit",
        default=False,
        type=check_positive,
        help="limit the playlist generated to only contain the allowed limit of videos",
    )
    parser.add_argument(
        "--regex",
        default="^.*(.mp4)|(.mkv)$",
        help="only consider files that match to the supplied regex pattern",
    )
    parser.add_argument(
        "--dry-run",
        default=False,
        action="store_true",
        help="Dont launch VLC, instead only print the playlist. Useful for testing regexs",
    )
    return parser.parse_args()


def get_file_paths(root_path, recursive, regex):
    """Grab a list of file paths under the root_path directory that match the
    supplied regex. If the recursive flag is true, walk all subdirs under the
    root path.
    """
    if recursive:
        file_paths = []
        for root, _, files in os.walk(root_path):
            for file in files:
                file_paths.append(os.path.join(root, file))
    else:
        maybe_file_paths = [os.path.join(root_path, f) for f in os.listdir(root_path)]
        file_paths = [f for f in maybe_file_paths if os.path.isfile(f)]

    return [f for f in file_paths if regex.match(f)]


def main():
    args = parse_args()
    path = args.path
    recursive = args.recursive
    limit = args.limit

    try:
        regex = re.compile(args.regex)
    except re.error:
        print(f"Failed to compile regex with pattern '{args.regex}'")
        return

    file_paths = get_file_paths(path, recursive, regex)

    if len(file_paths) == 0:
        print("No videos matched.  Check your path and/or regex.")
        print(f"     root path: {path}\n regex pattern: {args.regex}")
        return

    random.shuffle(file_paths)

    if limit and limit < len(file_paths):
        file_paths = file_paths[0:limit]

    if args.dry_run:
        print("Random Video Playlist")
        padded_len = len(str(len(file_paths)))
        for num, video in enumerate(file_paths):
            print(f"  {str(num+1).zfill(padded_len)}) {video}")
        return

    cmd = ["vlc"] + file_paths
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
