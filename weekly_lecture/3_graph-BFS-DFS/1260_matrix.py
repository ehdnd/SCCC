import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def DFS_matrix(v):
    print(v, end=" ")
    visit_1[v] = 1
    for i in range(len(matrix[v])):
        if matrix[v][i] == 1 and not visit_1[i]:
            DFS_matrix(i)


def BFS_matrix(v):
    q = deque()
    q.append(v)
    visit_2[v] = 1

    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in range(1, len(visit_2)):
            if matrix[v][i] == 1 and not visit_2[i]:
                visit_2[i] = 1
                q.append(i)


N, M, V = map(int, input().split())
visit_1 = [0] * (N + 1)
visit_2 = [0] * (N + 1)

# 인접 행렬로 받아보자
matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = matrix[v][u] = 1

DFS_matrix(V)
print()
BFS_matrix(V)


# # 행렬 출력확인
# for u in matrix:
#     for v in u:
#         print(v, end=" ")
#     print()
