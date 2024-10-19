import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def jud():
    N = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    res = 0
    while 1:
        if len(files) <= 1:
            break
        sum = heapq.heappop(files) + heapq.heappop(files)
        res += sum
        heapq.heappush(files, sum)

    return res


N = int(input())
for _ in range(N):
    print(jud())
