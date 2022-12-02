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
    print("Input:")

    if isinstance(data, list):
        if shorten:
            pprint(data[:PREVIEW_LIMIT_LIST])
            
            if len(data) > PREVIEW_LIMIT_LIST:
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

def string_to_list(s, regex = r"[\n\r]"):
    p_newline = re.compile(regex)

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

def entries_as_dicts(ls, regex = r":", types = (str, str)):

    out = []
    pattern_split = re.compile(regex)

    for entry in ls:
        d = dict()
        for raw in entry:
            k, v = pattern_split.split(raw)

            if types:
                k = types[0](k)
                v = types[1](v)

            d[k] = v

        out.append(d)

    return out

def map_split(ls, regex):
    pattern = re.compile(regex)
    return [pattern.split(x) for x in ls]

def map_sub(ls, regex, target):
    pattern = re.compile(regex)
    return [pattern.sub(target, x) for x in ls]

def map_join(ls, join = " "):
    return [join.join(x) for x in ls]

def map_inner2(type, ls):
    return [[type(x) for x in l] for l in ls]

def group_contents(ls, sep = None):
    out = []

    current = []

    for item in ls:
        if sep is not None and item == sep:
            out.append(current)
            current = []
        else:
            current.append(item)

    out.append(current)
    return out

def split(s, regex):
    p_split = re.compile(regex)
    return p_split.split(s)

def foldr(f, out, xs):
    for x in xs:
        out = f(x, out)

    return out

def map_split_to_tuple(xs, regex, types = (str,str)):

    pattern = re.compile(regex)

    for i,x in enumerate(xs):
        m = pattern.match(x)

        values = list(m.groups())

        for j,t in enumerate(types):
            values[j] = t(values[j])

        xs[i] = tuple(values)

    return xs