import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# for i in range(N):
#     B[i] = [B[i], i]

# B.sort(key=lambda x: x[0], reverse=True)
# A.sort()

A.sort()
B.sort(reverse=True)
cnt = 0
for i in range(N):
    cnt += A[i] * B[i]

print(cnt)
