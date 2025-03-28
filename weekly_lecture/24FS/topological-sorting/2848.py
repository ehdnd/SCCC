import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = [input() for _ in range(N)]
G = {}
indegree = {}

# 정점 생성
for word in words:
    for w in word:
        if w not in G:
            G[w] = []
            indegree[w] = 0

# 간선 생성?
isChanged = False
for i in range(1, N):
    w1 = words[i - 1]
    w2 = words[i]
    for j in range(min(len(w1), len(w2))):
        if w1[j] == w2[j]:
            continue
        G[w1[j]].append(w2[j])
        indegree[w2[j]] += 1
        isChanged = True
        break

    # 파악할 수 있는 순서 없음
    if not isChanged and len(w1) > len(w2):
        print("!")
        sys.exit()

q = deque()
for w in G.keys():
    if indegree[w] == 0:
        q.append(w)

res = []
isCycle = False
isMore = False
for _ in range(len(G)):
    if not q:
        isCycle = True
        break
    if len(q) > 1:
        isMore = True
        # break

    x = q.popleft()
    res.append(x)
    for nx in G[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

# 사이클 == 올바른 순서 없음
if isCycle:
    print("!")
    sys.exit()

if isMore:
    print("?")
    sys.exit()

print(*res, sep="")
