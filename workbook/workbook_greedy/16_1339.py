import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
chars = []
for _ in range(N):
    char = reversed(input())
    chars.append(char)

# 10A > A + B 려면 9A > B 무조건 성립하네.. 그냥 자릿수 큰놈에 큰수주자
# [문자 + 자릿수] MAX 자릿수 순으로 할당 10^자릿수로 계산
