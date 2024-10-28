import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(arr):
    stack = []
    for char in arr:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"


N = int(input())
for _ in range(N):
    arr = input()
    print(jud(arr))
