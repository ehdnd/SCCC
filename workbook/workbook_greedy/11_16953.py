import sys

input = lambda: sys.stdin.readline().rstrip()
A, B = map(int, input().split())

cnt = 1
while 1:
    if A >= B:
        break
    elif str(B).endswith("1"):
        B = int(str(B)[:-1])
    elif B % 2 == 0:
        B = B // 2
    else:
        break
    cnt += 1


if A == B:
    print(cnt)
else:
    print(-1)
