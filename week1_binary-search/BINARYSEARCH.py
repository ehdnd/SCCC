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
