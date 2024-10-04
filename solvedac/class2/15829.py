import sys

input = lambda: sys.stdin.readline().rstrip()
L = int(input())
str = input()
r = 31
M = 1234567891

res = 0
for i in range(L):
    char = str[i]
    res += (ord(char) - 96) * (r**i)
    res %= M

print(res)
