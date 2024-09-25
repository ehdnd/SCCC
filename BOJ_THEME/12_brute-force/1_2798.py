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

# # 다른 답
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             if cards[i] + cards[j] + cards[k] > M:
#                 continue
#             else:
#                 result = max(result, cards[i] + cards[j] + cards[k])
# print(result)


# # 다른 답
# from itertools import combinations
