import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
PN = "I" + "OI" * N
M = int(input())
P = input()

cnt = 0
for i in range(M - len(PN) + 1):
    if PN == P[i : i + len(PN)]:
        cnt += 1

print(cnt)
