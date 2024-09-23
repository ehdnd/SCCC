import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
cases = []
for _ in range(n):
    cases.append(list(input().split()))

for case in cases:
    str = case[1]
    R = int(case[0])
    for char in str:
        print(char * R, end="")
    print()
