# fail - 잘못된 break, 잘못된 루프
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    if num == 1:
        continue

    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        cnt += 1

print(cnt)
