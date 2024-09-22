import sys

input = sys.stdin.readline

while 1:
    try:
        a, b = map(int, input().strip().split())
        print(a + b)
    except:
        break
