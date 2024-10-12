import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
F = []
for _ in range(N):
    F.append(list(input()))
res = N * M


def jud(F, row_idx, col_idx):
    cnt_1 = 0
    cnt_2 = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if F[row_idx + i][col_idx + j] != "B":
                    cnt_1 += 1
                else:
                    cnt_2 += 1
            else:
                if F[row_idx + i][col_idx + j] != "W":
                    cnt_1 += 1
                else:
                    cnt_2 += 1
    return min(cnt_1, cnt_2)


for n in range(0, N - 7):
    row_idx = n
    for m in range(0, M - 7):
        col_idx = m
        temp = jud(F, row_idx, col_idx)
        if temp < res:
            res = temp

print(res)
