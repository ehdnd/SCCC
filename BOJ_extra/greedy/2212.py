import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
cover_lengths = []
for i in range(N - 1):
    cover_lengths.append(sensors[i + 1] - sensors[i])

cover_lengths.sort(reverse=True)
res = cover_lengths[K - 1 :]

print(sum(res))
