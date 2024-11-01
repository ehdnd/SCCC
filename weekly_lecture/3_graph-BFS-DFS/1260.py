import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


# def BFS_matrix(matrix, v, visit):
#     q = deque()
#     q.append(v)
#     visit[v] = 1

#     while q:
#         v = q.popleft()
#         print(v, end=" ")

#         for i in range(1, len(visit)):
#             if matrix[v][i] == 1 and not visit[i]:
#                 visit[i] = 1
#                 q.append(i)


def BFS_list(graph, v, visit):
    q = deque()
    q.append(v)
    visit[v] = 1

    while q:
        v = q.popleft()
        print(v, end=" ")

        for node in graph[v]:
            if not visit[node]:
                q.append(node)
                visit[node] = 1


# def DFS_matrix(matrix, v, visit):
#     print(v, end=" ")
#     visit[v] = 1
#     for i in range(len(matrix[v])):
#         if matrix[v][i] == 1 and not visit[i]:
#             DFS_matrix(matrix, i, visit)


def DFS_list(graph, v, visit):
    print(v, end=" ")
    visit[v] = 1
    for node in graph[v]:
        if not visit[node]:
            DFS_list(graph, node, visit)


N, M, V = map(int, input().split())
visit_1 = [0] * (N + 1)
visit_2 = [0] * (N + 1)

# # 인접 행렬로 받아보자
# matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# for _ in range(M):
#     u, v = map(int, input().split())
#     matrix[u][v] = matrix[v][u] = 1

# 인접 리스트로 받아보자
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N + 1):
    graph[i].sort()

# DFS_matrix(matrix, V, visit_1)
# print()
# BFS_matrix(matrix, V, visit_2)

DFS_list(graph, V, visit_1)
print()
BFS_list(graph, V, visit_2)


# # 행렬 출력확인
# for u in matrix:
#     for v in u:
#         print(v, end=" ")
#     print()

# # 리스트 확인
# print(graph)
# for u in graph:
#     print(graph.index(u), ":", end=" ")
#     for v in u:
#         print(v, end=" ")
#     print()
