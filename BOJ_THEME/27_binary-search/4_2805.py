import sys

input = sys.stdin.readline

N, total_need_tree_length = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid

    if cnt >= total_need_tree_length:
        start = mid + 1
    else:
        end = mid - 1
print(end)
