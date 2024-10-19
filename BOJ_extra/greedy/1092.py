import sys
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))


def jud(cranes, boxes):
    cnt = 0
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)
    while 1:
        if len(boxes) == 0:
            break
        for crane in cranes:
            for i in range(len(boxes)):
                if crane >= boxes[i]:
                    del boxes[i]
                    break
        cnt += 1

    return cnt


if max(cranes) < max(boxes):
    print(-1)
else:
    print(jud(cranes, boxes))
