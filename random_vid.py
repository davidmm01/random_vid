import argparse
import os
import random
import subprocess


def check_positive(value):
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
        "-l",
        "--limit",
        default=False,
        type=check_positive,
        help="limit the playlist generated to only contain the allowed limit of videos",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    path = args.path
    recursive = args.recursive
    limit = args.limit

    if recursive:
        file_paths = []
        for root, _, files in os.walk(path):
            for file in files:
                file_paths.append(os.path.join(root, file))
    else:
        maybe_file_paths = [os.path.join(path, f) for f in os.listdir(path)]
        file_paths = [f for f in maybe_file_paths if os.path.isfile(f)]

    # TODO: need a way to handle files that cant be played through vlc

    random.shuffle(file_paths)

    if limit and limit < len(file_paths):
        file_paths = file_paths[0:limit]

    cmd = ["vlc"] + file_paths
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
