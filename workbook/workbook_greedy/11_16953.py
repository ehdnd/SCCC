import sys

input = lambda: sys.stdin.readline().rstrip()
A, B = map(int, input().split())

cnt = 1
while 1:
    if A >= B:
        break

    if B % 2 == 0:
        B = B // 2
    else:
        if B < 10:
            break
        B = int(str(B)[:-1])
    cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)
