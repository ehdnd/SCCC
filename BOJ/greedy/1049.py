import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
lines = []
for i in range(M):
    lines.append(list(map(int, input().split())))

s_need = N // 6
o_need = N % 6

res = 0
min_o = min(lines, key=lambda x: x[1])[1]
min_s = min(lines, key=lambda x: x[0])[0]
res += min(min_o * 6, min_s) * s_need
res += min(min_s, min_o * o_need)

print(res)
