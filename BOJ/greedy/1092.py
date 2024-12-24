import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))


def jud(cranes, boxes, N):
    cnt = 0
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)
    idx = [0] * N
    while 1:
        if set(boxes) == {0}:
            break
        for j in range(N):
            crane = cranes[j]
            for i in range(idx[j], len(boxes)):
                if crane >= boxes[i] and boxes[i] != 0:
                    boxes[i] = 0
                    idx[j] = i
                    break
        cnt += 1

    return cnt


if max(cranes) < max(boxes):
    print(-1)
else:
    print(jud(cranes, boxes, N))
