import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    str = input()
    print(f"{str[0]}{str[len(str)-1]}")
