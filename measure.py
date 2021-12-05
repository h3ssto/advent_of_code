#!/usr/bin/env python3
import os
import re

import timeit

def find_all(name, path):
    out = []
    for root, dirs, files in os.walk(path):
        if name in files:
            out.append(os.path.join(root, name))
    return out


solvers = find_all("input", ".")

p_path = re.compile(r"^[.]/(?P<year>\d{4})/day(?P<day>\d+)/.*$")

puzzles = dict()

home = os.getcwd()

solvers = sorted(solvers)

for solver in solvers:
    m = p_path.match(solver)
    if m:
        year = m["year"]
        day  = m["day"]

    os.chdir(str(year))
    
    call = lambda: os.system(f"python -m day{day}.solve > /dev/null")

    reps, time_total = timeit.Timer(call).autorange()

    puzzles[(int(year), int(day))] = {
        "reps": reps,
        "total": time_total,
        "avg": time_total / reps
    }   

    os.chdir(home)

update = [["year", "day", "avg"]]

for (year, day), v in puzzles.items():
    avg = v["avg"]

    print(year, f"{day:2}:", f"{avg:0.3f}", end="")

    if avg >= 5:
        print("\t!!!")
    else:
        print()

    if day < 10:
        day = f"0{day}"

    update.append([str(year), str(day), f"{avg:.3f}"])

update = [",".join(x) for x in update]
update.append("")
update = f"{os.linesep}".join(update)

with open("performance.csv", "w+") as file:
    file.write(update)


