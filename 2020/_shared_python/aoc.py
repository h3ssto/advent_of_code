import pathlib
import re

from pprint import pprint
from termcolor import colored

PREVIEW_LIMIT = 1021
PREVIEW_LIMIT_LIST = 8

## Print Helper

def red(args):
    return colored(args, "red")

def green(args):
    return colored(args, "green")

def blue(args):
    return colored(args, "blue")

def preview_input(data, shorten = True):
    print("Input:", end = " ")

    if isinstance(data, list):
        if shorten:
            pprint(data[:PREVIEW_LIMIT_LIST])
            print(red("!!!"), len(data) - 8, red("entries redacted !!!"))
        else:
            print()
            pprint(data)

    else:
        print(f"{data[:min(len(data), PREVIEW_LIMIT)]}", red("...") if len(data) > PREVIEW_LIMIT else "", sep = "")

    print("-" * 64)

## IO Helper

def input_from_file(root_file):
    directory = pathlib.Path(root_file).parent.resolve()

    try:
        with open(f"{directory}/input") as file:
            raw = file.readlines()
    except Exception as e:
        return str(e)

    p_newline = re.compile(r"[\n\r]")

    return [p_newline.sub("", x) for x in raw]

def string_to_list(s):
    p_newline = re.compile(r"[\n\r]")

    return p_newline.split(s)

## Converison

def map2(type, ls):
    return [type(x) for x in ls]

def entries_as_tuples(ls, types = None):

    if types:
        for item in ls:
            for i, t in enumerate(types):
                item[i] = t(item[i])

    return [tuple(x) for x in ls]

def map_split(regex, ls):
    pattern = re.compile(regex)
    return [pattern.split(x) for x in ls]

