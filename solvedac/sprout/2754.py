# 딕셔너리를 이용하자..

import sys

input = lambda: sys.stdin.readline().rstrip()

grade = input()
n = 0
a = grade[0]

if a == "A":
    n += 4
elif a == "B":
    n += 3
elif a == "C":
    n += 2
elif a == "D":
    n += 1
else:
    n = f"{n}.0"

if len(grade) == 2:
    b = grade[1]
    if b == "+":
        n += 0.3
    elif b == "-":
        n -= 0.3
    else:
        n = f"{n}.0"

print(n)
