import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
arr = list(map(int, input().split()))
diff = []
for i in range(N - 1):
    diff.append(arr[i + 1] - arr[i])

diff.sort(reverse=True)
res = sum(diff[K - 1 :])

print(res)
