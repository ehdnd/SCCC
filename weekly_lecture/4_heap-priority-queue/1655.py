import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def move(left, mid, right):
    l_len = len(left)
    r_len = len(right)
    if l_len + 1 < r_len:
        t = heapq.heappop(right)
        heapq.heappush(left, -mid)
        mid = t
    elif l_len > r_len:
        t = -heapq.heappop(left)
        heapq.heappush(right, mid)
        mid = t

    return mid


def jud():
    left = []
    right = []
    mid = None
    for _ in range(N):
        M = int(input())
        if not mid:
            mid = M
        elif M < mid:
            heapq.heappush(left, -M)
        else:
            heapq.heappush(right, M)
        mid = move(left, mid, right)
        print(mid)
    return


N = int(input())
jud()
