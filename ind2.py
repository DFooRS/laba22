#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pathlib
from pathlib import Path
import sys


def dir_tree(path, prefix = ''):
    """
    Функция вывода дерева каталогов.
    """
    items = list(path.iterdir())
    pointers = [tee] * (len(items) - 1) + [last]
    for i, item in enumerate(items):
        print(prefix + pointers[i] + item.name)
        if item.is_dir():
            if pointers[i] == tee:
                add_pref = branch
            else:
                add_pref = space
            dir_tree(item, prefix + add_pref)

def main(command_line=None):
    """
    Главная функция программы.
    """
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "Path",
        action="store",
        help="Путь к директории"
    )
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")

    tree = subparsers.add_parser(
        "tree",
        parents=[file_parser],
        help="Отобразить дерево каталога"
    )

    args = parser.parse_args(command_line)

    if args.command == 'tree':
        path = pathlib.Path(args.Path)
        dir_tree(path)


if __name__ == '__main__':
    space = '    '
    branch = '│   '
    tee = '├── '
    last = '└── '
    main()
