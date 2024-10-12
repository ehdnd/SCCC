import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
arr = list(map(int, input().split()))

# kadane's algorithm
# [-2, 2, 4, -11, 6] 에서
# -11 에서 다시 시작할 지
# globalMax는 아니지만 이전 subarrayh와 이어서 진행할 지 결정
# => local_max + current_num 과 current_num 비교
# 결국 이전 subarray 중 최대인 값을 가지는 것과 현재 숫자를 비교

sub_arr_max = arr[0]
global_max = sub_arr_max

for i in range(1, N):
    current_num = arr[i]

    # 더한 값은 sub arr 이어가기
    # current_num 은 sub arr 새로 시작하기
    sub_arr_max = max(sub_arr_max + current_num, current_num)

    # global_max 갱신하기
    global_max = max(global_max, sub_arr_max)

print(global_max)
