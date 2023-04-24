#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from datetime import datetime

def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory/name_pattern.format(counter)
        if not path.exists():
            return path


path = unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')