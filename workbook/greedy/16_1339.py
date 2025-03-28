import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
chars = []
for _ in range(N):
    char = input()[::-1]
    chars.append(char)

# 10A > A + B 려면 9A > B 무조건 성립하네.. 그냥 자릿수 큰놈에 큰수주자
# [문자 + 자릿수] MAX 자릿수 순으로 할당 10^자릿수로 계산

dic = {}
for char in chars:
    for i in range(len(char)):
        if char[i] not in dic:
            dic[char[i]] = 10**i
        else:
            dic[char[i]] += 10**i

arr = sorted(dic.items(), reverse=True, key=lambda x: x[1])

k = 9
res = 0
for i in range(len(arr)):
    res += k * arr[i][1]
    k -= 1

print(res)
