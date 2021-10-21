#Usage:
#In linux terminal type:
#python3 (path of python file) (path of sort file)
#No parentheses needed around the path of the sort file. Type the path same as the python file itself.

import fileinput

names = []
temp = ""
for line in fileinput.input():
    temp = line.strip()
    if len(temp) > 0:
        names.append(temp)

final = sorted(names, key=lambda x: (len(x), x))

print(*final, sep="\n")

