import sys

input = sys.stdin.readline

n = int(input())

sums = []
for i in range(n):
    a, b = map(int, input().strip().split())
    sums.append(a + b)

for sum in sums:
    print(sum)
