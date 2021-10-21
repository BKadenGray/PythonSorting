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

