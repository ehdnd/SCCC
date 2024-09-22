import sys

input = lambda: sys.stdin.readline().rstrip()

a = [x for x in range(1, 31)]

for i in range(28):
    a.remove(int(input()))

for num in a:
    print(num, end=" ")
