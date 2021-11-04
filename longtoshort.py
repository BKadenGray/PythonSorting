test = 'diftest2.sh'
names = []
temp = ""
for line in fileinput.input():
    temp = line.strip()
    if len(temp) > 0:
        names.append(temp)

print("Longest to Shortest Method")
final = sorted(names, key=lambda x: (len(x), x), reverse=True)

print(*final, sep="\n")

original_stdout = sys.stdout
with open('sorted.txt', 'w+') as x:
    x.truncate(0)
    sys.stdout = x
    print(*final, sep="\n")
    sys.stdout = original_stdout

subprocess.call(['sh', test])
