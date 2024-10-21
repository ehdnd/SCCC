import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, input().split())))

rooms.sort(key=lambda x: (x[1], x[2]))

heap = [rooms[0][2]]
for i in range(1, N):
    room = rooms[i]
    if room[1] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, room[2])

print(len(heap))
