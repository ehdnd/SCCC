import sys

input = lambda: sys.stdin.readline().rstrip()
A, B, V = map(int, input().split())
jump = A - B
temp_V = V - A
day = temp_V // jump
if temp_V % jump == 0:
    day += 1
else:
    day += 2

print(day)
