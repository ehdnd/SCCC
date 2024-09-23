import sys

input = lambda: sys.stdin.readline().rstrip()

str = input()

res = [-1] * 26  # 0부터 25까지 26개

# 소문자 ord("a") == 97 , ord("z") == 122

for char in str:
    idx = ord(char) - ord("a")
    if res[idx] == -1:
        res[idx] = str.index(char)

for n in res:
    print(n, end=" ")
