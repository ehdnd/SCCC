import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, input().split())))

rooms.sort(key=lambda x: (x[0], x[1]))

heap = [rooms[0][1]]
for i in range(1, N):
    room = rooms[i]
    if room[0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, room[1])

print(len(heap))
