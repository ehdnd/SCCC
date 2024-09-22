import sys

input = lambda: sys.stdin.readline().rstrip()

str = input()

temp = []
for x in str:
    if x.isupper():
        temp.append(x.lower())
    else:
        temp.append(x.upper())

print("".join(temp))
