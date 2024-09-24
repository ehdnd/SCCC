import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tasks = []
for i in range(N):
    a, b = map(int, input().split())
    tasks.append([a, b, i + 1])

tasks.sort(reverse=True, key=lambda x: (x[1] / x[0], -x[2]))

for task in tasks:
    print(task[2], end=" ")
