# recursion
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


# while loop
def binary_search(target, data):
    data.sort()
    start = 0  # 맨 처음 위치
    end = len(data) - 1  # 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2  # 중간값

        if data[mid] == target:
            return mid  # target 위치 반환

        elif data[mid] > target:  # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:  # target이 크면 오른쪽을 더 탐색
            start = mid + 1

    return None
