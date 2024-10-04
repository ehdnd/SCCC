import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(str):
    cnt1 = 0
    cnt2 = 0
    for char in str:
        if char == "(":
            cnt1 += 1
        elif char == ")":
            cnt1 -= 1
        elif char == "[":
            cnt2 += 1
        elif char == "]":
            cnt2 -= 1

        if cnt1 < 0 or cnt2 < 0:
            return "no"

    if cnt1 == 0 and cnt2 == 0:
        return "yes"
    else:
        return "no"


while 1:
    string = input()
    if string == ".":
        break
    print(jud(string))
