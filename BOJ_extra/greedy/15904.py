import sys

input = lambda: sys.stdin.readline().rstrip()
strings = list(input().split())

res = []
for string in strings:
    for char in string:
        if char.isupper():
            res.append(char)

U, C, P = False, False, False
for char in res:
    if char == "U" and not U:
        U = True
    elif char == "C" and U and not C:
        C = True
    elif char == "P" and C and not P:
        P = True
        C = False

if U and C and P:
    print("I love UCPC")
else:
    print("I hate UCPC")
