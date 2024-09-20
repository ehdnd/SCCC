import sys

input = sys.stdin.readline

a = [int(input()) for _ in range(5)]

avg = sum(a) / len(a)

sorted_a = sorted(a)

mid = sorted_a[2]

print(int(avg))
print(mid)
