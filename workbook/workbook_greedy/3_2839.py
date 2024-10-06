import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

five = N // 5
left = N % 5
three = -1

while 1:
    if left % 3 == 0:
        three = left // 3
        break
    else:
        if five == 0:
            break
        five -= 1
        left += 5

print(five + three)
