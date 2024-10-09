import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
cards = [0] * N
for i in range(N):
    cards[i] = int(input())
