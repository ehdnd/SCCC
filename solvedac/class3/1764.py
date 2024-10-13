import sys

input = lambda: sys.stdin.readline().rstrip()
A, B = map(int, input().split())
heard = set()
seen = set()
for _ in range(A):
    heard.add(input())
for _ in range(B):
    seen.add(input())

res = sorted(list(heard.intersection(seen)))
print(len(res))
for name in res:
    print(name)
