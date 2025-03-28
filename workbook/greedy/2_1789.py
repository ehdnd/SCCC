import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

# num = 0
total = 0
cnt = 0
if N == 1:
    cnt += 1

for i in range(1, N):
    total += i
    # num = i
    cnt = i
    if total > N:
        total -= i
        # num -= 1
        cnt -= 1
        break

print(cnt)

# # 남은 수가 num 범위에 있는지
# if N - total <= num:
#     cnt -= 1
#     print(N - total, num)
# else:
#     print(num, cnt, total, N - total)
