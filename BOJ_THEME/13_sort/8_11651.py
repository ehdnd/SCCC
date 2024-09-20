# sort 함수 key 값으로 함수.. 람다 함수가 가능하다
# x[1] 만 사용할 경우 x[1] 이 같다면 원래 순서 유지한다
import sys

input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
    a, b = map(int, input().strip().split())
    list.append([a, b])

list.sort(key=lambda x: (x[1], x[0]))

for i in list:
    print(i[0], i[1])
