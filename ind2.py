#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pathlib
from pathlib import Path
import sys


def dir_tree(path, prefix=' '):
    """
    Функция вывода дерева каталогов.
    """
    print(f'{prefix}├── {Path(path).name}')
    for item in Path(path).iterdir():
        if item.is_dir():
            dir_tree(item, prefix + '│  ')
        else:
            print(f'{prefix}│  ├──{item.name}')


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
    main()
