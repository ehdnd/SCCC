import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def jud(K):
    N = int(input())
    files = list(map(int, input().split()))

    if N == 1:
        return 1

    heapq.heapify(files)
    res = 1
    while 1:
        if len(files) <= 1:
            break
        sum = (heapq.heappop(files) % K) * (heapq.heappop(files) % K)
        res = (res * (sum % K)) % K
        heapq.heappush(files, sum)

    return res % K


K = 1000000007
N = int(input())
for _ in range(N):
    print(jud(K))
