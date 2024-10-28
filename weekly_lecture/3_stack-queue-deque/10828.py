import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    N = int(input())
    stack = []
    for _ in range(N):
        d = input()
        if d == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif d == "size":
            print(len(stack))
        elif d == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif d == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        else:
            stack.append(int(d.split()[1]))


jud()
