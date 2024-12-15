import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def modify_num(num: str) -> str:
    l = len(num)
    cnt = 0
    res = ""
    while len(res) < 10:
        res += num[cnt % l]
        cnt += 1
    return res


# 자릿수 큰걸 여러번 쓰자 -> 사용할 개수 찾기
# 1231231231 처럼 modify 하고 순서 정하자


def solve() -> None:
    K, N = MIS()
    nums = []
    for _ in range(K):
        string = input()
        nums.append([string, modify_num(string), 1])

    nums.sort(key=lambda x: (len(x[0]), x[1]), reverse=True)
    nums[0][2] += N - K

    nums.sort(key=lambda x: x[1], reverse=True)

    res = ""
    for num, _, cnt in nums:
        res += num * cnt
    print(res)

    return


if __name__ == "__main__":
    solve()
