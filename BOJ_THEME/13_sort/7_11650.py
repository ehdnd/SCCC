# sort.. 리스트도 되는구나.. 기준도 설정 가능하네..
import sys

input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
    a, b = map(int, input().strip().split())
    list.append([a, b])

list.sort()

for i in list:
    print(i[0], i[1])
