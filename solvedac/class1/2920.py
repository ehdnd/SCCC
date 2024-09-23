import sys

input = lambda: sys.stdin.readline().rstrip()

arr = list(map(int, input().split()))
a = [x for x in range(1, 9)]
b = sorted(a, reverse=True)

if arr == a:
    print("ascending")
elif arr == b:
    print("descending")
else:
    print("mixed")
