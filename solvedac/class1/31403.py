import sys

input = lambda: sys.stdin.readline().rstrip()

arr = []
for i in range(3):
    arr.append(input())

A = arr[0]
B = arr[1]
C = arr[2]

print(int(A) + int(B) - int(C))
print(int(A + B) - int(C))
