import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

money = 0
min_price = prices[0]
for i in range(N - 1):
    if prices[i] < min_price:
        min_price = prices[i]
    money += min_price * lengths[i]

print(money)
