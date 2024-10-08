import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
money = 0
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price_idx = -1
while 1:
    total_length = sum(lengths)
    if total_length <= 0:
        break
    prices = prices[:min_price_idx]
    min_price_idx = prices.index(min(prices))
    money += sum(prices[min_price_idx] * lengths[min_price_idx:])
    lengths = lengths[:min_price_idx]

print(money)
