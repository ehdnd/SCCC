import sys

# from bisect import bisect_left, bisect_right


def binary_search(arr, lower_idx, upper_idx, target):
    if lower_idx <= upper_idx:
        mid = lower_idx + (upper_idx - lower_idx) // 2

        if arr[mid] == target:
            # return middle index
            return mid
        elif target < arr[mid]:
            # binary_search recursion lower half
            return binary_search(arr, lower_idx, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, upper_idx, target)

    else:
        # not in the [arr]
        return -1


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().strip().split()))
num = int(input())
targets = list(map(int, input().strip().split()))

a.sort()

for target in targets:
    if binary_search(a, 0, n - 1, target) != -1:
        print(1)
    else:
        print(0)
