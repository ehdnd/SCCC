import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

dic = {}
dic_2 = {}
for i in range(1, N + 1):
    a = input()
    dic[i] = a
    dic_2[a] = i

question = []
for i in range(M):
    question.append(input())

for q in question:
    if q.isdigit():
        print(dic[int(q)])

    else:
        print(dic_2[q])
