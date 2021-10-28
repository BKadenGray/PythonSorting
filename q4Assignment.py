# Usage:
# In linux terminal type:
# python3 (path of python file) (path of sort file)
# No parentheses needed around the path of the sort file. Type the path same as the python file itself.
# For proper test paths, change the string in test1 and test2

import fileinput
import sys
import subprocess

test1 = '/home/azakan/diftest1.sh'
test2 = '/home/azakan/diftest2.sh'
names = []
temp = ""
for line in fileinput.input():
    temp = line.strip()
    if len(temp) > 0:
        names.append(temp)


def menu():
    print("1 - Shortest to Longest")
    print("2 - Longest to Shortest")
    print("3 - Quit")


menu()
while True:
    try:
        option = int(input("Select a method of sorting"))
        while option < 1 or option > 3:
            option = int(input("Invalid, try again!"))
        if option == 3:
            raise SystemExit(0)
        elif option == 1:
            final = sorted(names, key=lambda x: (len(x), x))
        elif option == 2:
            final = sorted(names, key=lambda x: (len(x), x), reverse=True)
    except ValueError:
        print("Invalid input, try again")
        continue
    else:
        break

print(*final, sep="\n")

original_stdout = sys.stdout
with open('sorted.txt', 'w+') as x:
    x.truncate(0)
    sys.stdout = x
    print(*final, sep="\n")
    sys.stdout = original_stdout


while True:
    try:
        menu()
        option = int(input("Select test option:"))
        while option < 1 or option > 3:
            option = int(input("Invalid, try again!"))
        if option == 3:
            raise SystemExit(0)
        elif option == 1:
            subprocess.call(['sh', test1])
        elif option == 2:
            subprocess.call(['sh', test2])
    except ValueError:
        print("Invalid input, try again")
        continue
    else:
        break
