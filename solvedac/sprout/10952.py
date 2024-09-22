# 오잉.. 콘솔이랑 답이 좀 다르네.. 백준 입력이 뭔지 모르겠네
import sys

input = sys.stdin.readline

while 1:
    a, b = map(int, input().strip().split())
    if a == 0:
        break
    print(a + b)
