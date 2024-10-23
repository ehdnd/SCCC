import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
lectures = []
for _ in range(N):
    s, e = map(int, input().split())
    lectures.append((s, e))
lectures.sort(reverse=True, key=lambda x: (x[0], x[1]))

temp = [lectures.pop()[1]]
while lectures:
    if lectures[-1][0] >= temp[0]:
        heapq.heappop(temp)

    heapq.heappush(temp, lectures.pop()[1])

print(len(temp))
