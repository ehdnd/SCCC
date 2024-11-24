import sys
from math import sqrt

input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    return S[a]


def Union(a, b):
    a, b = Find(a), Find(b)
    if a == b:
        return 0
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return 1


def jud():
    Lines = []

    # 벽 - 벽
    Lines.append([W, 0, N + 1])
    # 벽1 / 벽2 - 원
    for i in range(1, N + 1):
        x, y, r = Sensors[i]
        w1 = x - r
        w2 = W - x - r
        Lines.append([w1, 0, i]) if w1 > 0 else Lines.append([0, 0, i])
        Lines.append([w2, i, N + 1]) if w2 > 0 else Lines.append([0, i, N + 1])
    # 원 - 원
    for i in range(1, N + 1):
        x1, y1, r1 = Sensors[i]
        for j in range(i, N + 1):
            if i == j:
                continue
            x2, y2, r2 = Sensors[j]
            w = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) - r1 - r2
            Lines.append([w, i, j]) if w > 0 else Lines.append([0, i, j])
    # 간선 정렬
    Lines.sort()

    # 유니온파인드
    for w, a, b in Lines:
        Union(a, b)
        if -S[Find(a)] == N + 2:
            break

    return w / 2 if w != 0 else 0


T = int(input())
for _ in range(T):
    W, N = int(input()), int(input())
    Sensors = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
    # idx 0 왼벽, idx N+1 오벽
    S = [-1] * 101010
    print(jud())
