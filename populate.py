#!/usr/bin/env python3
import os
import re
import requests
import time

from dotenv import load_dotenv

#------------------------------------------------------------------------------#

def find_all(pattern, path):
    pattern = re.compile(pattern)

    out = []
    for root, dirs, files in os.walk(path):
        files = [file for file in files if pattern.match(file)]

        if files:
            out.append(root)

    return out

#------------------------------------------------------------------------------#

load_dotenv()

session = os.getenv("SESSION")

if not session:
    print("Key \"SESSION\" not found in \'./.env\', aborting.")
    exit()

url = "https://adventofcode.com/{year}/day/{day}/input"

paths = find_all(r"solve[.](py|hs|rs)", ".")

home = os.getcwd()
paths = sorted(paths)

p_year_day = re.compile(r"[.]/(?P<year>\d{4})/day(?P<day>\d{2})$")

wait = False

for path in paths:

    if wait:
        print("\tWaiting 10s to not spam requests...", end="\t")
        time.sleep(10)
        print("Done")
        wait = False

    print(path, end = "\t")

    m = p_year_day.match(path)

    day = int(m["day"])
    year = int(m["year"])

    if os.path.exists(os.path.join(path, "input")):
        print("Skipped")
    else:
        print("Acquiring...", end = "\t")

        req = requests.get(url.format(year = year, day = day), cookies = {"session":session})

        if req.status_code == 200:
            with open(os.path.join(path,"input"), "w+") as file:
                file.write(req.content.decode("utf-8"))

            wait = True
            print("Done")
        else:
            print("Failed w/:", req.status_code)
            exit()
