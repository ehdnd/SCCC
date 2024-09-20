# # 계수 정렬을 사용하자
# import sys

# input = sys.stdin.readline

# n = int(input())
# a = [int(input()) for _ in range(n)]
# max_value = max(a)


# def counting_sort(array, max):

#     # counting array 생성
#     counting_array = [0] * (max + 1)

#     # counting array에 input array내 원소의 빈도수 담기
#     for i in array:
#         counting_array[i] += 1

#     # counting array 업데이트.
#     for i in range(max):
#         counting_array[i + 1] += counting_array[i]

#     # output array 생성
#     output_array = [-1] * len(array)

#     # output array에 정렬하기(counting array를 참조)
#     for i in array:
#         output_array[counting_array[i] - 1] = i
#         counting_array[i] -= 1
#     return output_array


# organized = counting_sort(a, max_value)

# for i in organized:
#     print(i)

import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * 10000

for _ in range(n):
    num = int(input())
    arr[num - 1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i + 1)
