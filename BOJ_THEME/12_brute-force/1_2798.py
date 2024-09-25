import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

sums = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            sums.append(cards[i] + cards[j] + cards[k])

sums = set(sums)
sums = sorted(list(sums))

if M in sums:
    print(sums[bisect_left(sums, M)])
else:
    print(sums[bisect_left(sums, M) - 1])
