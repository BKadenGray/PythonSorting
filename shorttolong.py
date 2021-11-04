import fileinput
import sys
import subprocess

test1 = 'diftest1.sh'
names = []
temp = ""
for line in fileinput.input():
    temp = line.strip()
    if len(temp) > 0:
        names.append(temp)
        names.append(temp)

print("Shortest to Longest Method")
final = sorted(names, key=lambda x: (len(x), x))

print(*final, sep="\n")

original_stdout = sys.stdout
with open('sorted.txt', 'w+') as x:
    x.truncate(0)
    sys.stdout = x
    print(*final, sep="\n")
    sys.stdout = original_stdout

subprocess.call(['sh', test1])
