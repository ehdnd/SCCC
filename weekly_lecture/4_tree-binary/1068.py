import sys

input = lambda: sys.stdin.readline().rstrip()


# v 서브트리 노드의 합 반환
def dfs(v):
    res = 0
    if v == cut:
        return res

    if not G[v]:
        res = 1

    for nv in G[v]:
        res += dfs(nv)
    return res


N = int(input())
temp = list(map(int, input().split()))
cut = int(input())
G = [[] for _ in range(50)]
for i in range(N):
    if temp[i] == -1:
        root = i
        continue
    G[temp[i]].append(i)

print(dfs(root))
