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


N, M = map(int, input().split())
Know = list(map(int, input().split()))
Groups = [list(map(int, input().split())) for _ in range(M)]
S = [-1] * 51

for i in range(1, Know[0]):
    Union(Know[i], Know[i + 1])

for Group in Groups:
    for i in range(1, Group[0]):
        Union(Group[i], Group[i + 1])

key = Find(Know[-1])
for Group in Groups:
    for i in range(1, Group[0] + 1):
        if Find(Group[i]) == key:
            Union(key, Group[i])
            break

res = 0
for Group in Groups:
    if Find(Group[1]) != key:
        res += 1

print(res)
