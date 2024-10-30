import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(arr):
    stack = []
    for char in arr:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return "no"
        elif char == "[":
            stack.append("[")
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return "no"
        else:
            continue

    return "no" if stack else "yes"


while 1:
    arr = input()
    if arr == ".":
        break
    print(jud(arr))
