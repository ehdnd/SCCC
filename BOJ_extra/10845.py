import sys
import queue

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
q = queue.Queue()

for i in range(N):
    f = input()
    if f == "pop":
        if q.empty():
            print(-1)
        else:
            print(q.get())
    elif f == "size":
        print(q.qsize())
    elif f == "empty":
        if q.empty():
            print(1)
        else:
            print(0)
    elif f == "front":
        if q.empty():
            print(-1)
        else:
            print(q.queue[0])
    elif f == "back":
        if q.empty():
            print(-1)
        else:
            print(q.queue[-1])
    else:
        q.put(int(f.split()[1]))
