from _shared_python.aoc import *

#------------------------------------------------------------------------------#

input = input_from_file(__file__)

# ------------------------------------------------------------------------------#

output1 = 0
output2 = 0

#------------------------------------------------------------------------------#

pwd = ["/"]
dirs = {}
dir_sizes = {}

for line in input:
    if m := re.match(r"\$ cd (?P<path>[\w/.]+)", line):
        path = m["path"]

        if path == "/":
            pwd = ["/"]
        elif path == "..":
            pwd.pop()
        else:
            pwd.append(path)
    elif line == "$ ls":
        continue
    elif m := re.match(r"dir (?P<name>\w+)", line):
        cwd = f"{len(pwd)}{str(pwd)}"
        pwd.append(m["name"])
        files = dirs.get(str(cwd), [])
        files.append((f"{len(pwd)}{str(pwd)}", None))
        dirs[cwd] = files
        pwd.pop()
    elif m := re.match(r"(?P<size>\d+)\s+(?P<name>[\w.]+)", line):
        cwd = f"{len(pwd)}{str(pwd)}"

        files = dirs.get(cwd, [])
        files.append((m["name"], int(m["size"])))
        dirs[cwd] = files
    else:
        raise Exception(line)

dir_names = sorted(list(dirs.keys()), reverse = True)

for d in dir_names:
    for f in dirs[d]:
        n,s = f
        if s:
            dir_sizes[d] = dir_sizes.get(d, 0) + s
        else:
            dir_sizes[d] = dir_sizes.get(d, 0) + dir_sizes[n]

sizes = dir_sizes.values()

output1 = sum([x for x in sizes if x <= 100000])


### Part 2

delta = 30000000 - (70000000 - max(sizes))
output2 = min([s for s in sizes if s >= delta])

#------------------------------------------------------------------------------#

print("-" * 64)
print("Output 1:", green(output1))
print("Output 2:", green(output2))