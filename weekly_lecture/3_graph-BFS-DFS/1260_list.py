import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def DFS_list(v):
    print(v, end=" ")
    visit_1[v] = 1
    for i in graph[v]:
        if not visit_1[i]:
            DFS_list(i)


def BFS_list(v):
    q = deque()
    q.append(v)
    visit_2[v] = 1

    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visit_2[i]:
                q.append(i)
                visit_2[i] = 1


N, M, V = map(int, input().split())
visit_1 = [0] * (N + 1)
visit_2 = [0] * (N + 1)

# 인접 리스트로 받아보자
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

DFS_list(V)
print()
BFS_list(V)

# # 리스트 확인
# print(graph)
# for u in graph:
#     print(graph.index(u), ":", end=" ")
#     for v in u:
#         print(v, end=" ")
#     print()
