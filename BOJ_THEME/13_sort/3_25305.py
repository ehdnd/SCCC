import sys

input = sys.stdin.readline

n, prized = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

print(a[prized - 1])
