import sys

input = lambda: sys.stdin.readline().rstrip()

n, K = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

coin_num = 0
for coin in coins:
    coin_num += K // coin
    K = K % coin

print(coin_num)
