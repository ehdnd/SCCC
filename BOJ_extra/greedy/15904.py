import sys

input = lambda: sys.stdin.readline().rstrip()

i = 0
for char in input():
    if char == "UCPC"[i]:
        i += 1
    if i >= 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")
