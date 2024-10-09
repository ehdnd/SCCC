import sys

input = lambda: sys.stdin.readline().rstrip()
A = input()
B = input()

while 1:
    if len(A) >= len(B):
        break

    if B[-1] == "A":
        B = B[:-1]
    else:
        B = B[:-1][::-1]

if A == B:
    print(1)
else:
    print(0)
