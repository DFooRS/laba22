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
        if item.is_file():
            file = set_icon(item)
            print(prefix + pointers[i] + file + item.name)
        else:
            print(prefix + pointers[i] + folder + item.name)
            if pointers[i] == tee:
                add_pref = branch
            else:
                add_pref = space
            dir_tree(item, prefix + add_pref)


def set_icon(item):
    """
    Функция выбора иконки.
    """
    match item.suffix:
        case ".py":
            icon = "🐍"
        case item.suffix if item.suffix in text_files:
            icon = "📄"
        case item.suffix if item.suffix in video_files:
            icon = "🎥"
        case item.suffix if item.suffix in picture_files:
            icon = "📷"
        case ".exe":
            icon = "💻"
        case item.suffix if item.suffix in sharp_files:
            icon = "#"
        case item.suffix if item.suffix in razmetka:
            icon = "📐"
        case ".lnk":
            icon = "🔻"
        case ".img":
            icon = "💿"
        case _:
            icon = "❔"

    return icon


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
    folder = "📁"
    text_files = [".doc", ".docx", ".txt", "pdf", ".xlsx"]
    video_files = [".mp4", ".mov", ".mpeg-4", ".avi", ".mkv"]
    picture_files = [".jpeg", ".png", ".gif", ".svg", ".ico", ".jpg"]
    sharp_files = [".cs", ".sln"]
    razmetka = [".xaml", ".html"]
    main()
