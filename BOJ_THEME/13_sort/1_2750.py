def merge(left_arr, right_arr):
    merged = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1

    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])

    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    # recursion
    return merge(left, right)


import sys

input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

sorted = merge_sort(a)

for i in range(n):
    print(sorted[i])
