import sys

input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    return Find(S[a])


def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a == b:
        return False
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


N = int(input())
M = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
Q = list(map(int, input().split()))

S = [-1] * 201
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            Union(i + 1, j + 1)

isPossible = True
for i in range(1, M):
    a, b = Q[i - 1], Q[i]
    if Find(a) != Find(b):
        isPossible = False
        break

print("YES") if isPossible else print("NO")
