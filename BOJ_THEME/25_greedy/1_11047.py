import sys

input = lambda: sys.stdin.readline().rstrip()

n, K = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
