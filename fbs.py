#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from sys import exit
from os import stat,walk,path

badFilePath = "<NON UTF-8 FILEPATH>"

try:
    if argv[1] == "--version":
        print("FatBoySize 1.0.0.0 demensdeum@gmail.com 5 July 2022")
        exit(0)
except:
    pass

verbose = False

try:
    if argv[1] == "--verbose" or argv[1] == "-v":
        verbose = True
except:
    pass

def humanReadableSize(bytes, sizes = ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"], index = 0):
    size = bytes / 1024
    if size < 1024:
        return f"{str(size)[:4]} {sizes[index]}"
    elif index < len(sizes) - 1:
        return humanReadableSize(size, sizes, index + 1)
    else:
        return "UHH TOO LARGE!!!"

dirToSize = dict()

def firstPathComponent(somePath):    
    components = path.split(somePath)

    if components[0] != ".":
        return firstPathComponent(components[0])
    else:
        return components[1]

for root, dirs, files in walk("."):
    for file in files:
        filePath = path.join(root, file)
        key = firstPathComponent(filePath)
        size = dirToSize.get(key, 0)

        if verbose:
            try:
                print(filePath)
            except:
                print(badFilePath)
        try:
            size += stat(filePath).st_size
        except:
            pass

        dirToSize[key] = size

items = list(dirToSize.items())
items.sort(key=lambda x: x[1], reverse=True)

if verbose:
    print("---\nResult\n---")
for directory, size in items:
    try:
        print("{:<30} -> {:<30}".format(directory[:30], humanReadableSize(size)))
    except:
        print("{:<30} -> {:<30}".format(badFilePath, humanReadableSize(size)))

exit(0)