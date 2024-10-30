import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(N):
    stack = []
    for _ in range(N):
        k = int(input())
        if k == 0:
            stack.pop()
        else:
            stack.append(k)
    res = sum(stack)
    return res


N = int(input())
print(jud(N))
