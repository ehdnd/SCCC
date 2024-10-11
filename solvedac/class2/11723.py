import sys

input = lambda: sys.stdin.readline().rstrip()
M = int(input())
arr = [0 for i in range(21)]

for _ in range(M):
    req = list(input().split())
    f = req[0]
    if f == "add":
        arr[int(req[1])] = 1
    elif f == "remove":
        arr[int(req[1])] = 0
    elif f == "check":
        if arr[int(req[1])] == 1:
            print(1)
        else:
            print(0)
    elif f == "toggle":
        if arr[int(req[1])] == 1:
            arr[int(req[1])] = 0
        else:
            arr[int(req[1])] = 1
    elif f == "all":
        arr = [1 for i in range(21)]
    else:
        arr = [0 for i in range(21)]
