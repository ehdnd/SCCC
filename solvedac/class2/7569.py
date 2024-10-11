import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
# dic = {}
# for i in range(N):
#     dic[i] = list(map(int, input().split()))

# arr = sorted(dic.items(), reverse=True, key=lambda x: x[1])
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(N):
    k = 1
    for j in range(N):
        if i == j:
            continue
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            k += 1

    arr[i].append(k)

for i in range(N):
    print(arr[i][2], end=" ")
