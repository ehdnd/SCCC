import sys

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())

# 다 저장일단
memo = {}


def f(n_str: str) -> int:
    n = int(n_str)
    # base
    if n < 10:
        return n * (n + 1) // 2

    # 존재
    if n_str in memo:
        return memo[n_str]

    zegop = 10 ** (len(n_str) - 1)
    first_digit = n // zegop

    # 첫 번째
    res = f(str(zegop - 1)) * first_digit
    #
    res += (first_digit * (first_digit - 1) // 2) * zegop

    # 나머지 구해와라
    left = n % zegop
    res += first_digit * (left + 1)
    res += f(str(left))

    memo[n_str] = res
    return res


def solve() -> None:
    K = II()

    zari = 1
    while 1:
        zari_block = zari * 9 * (10 ** (zari - 1))
        if K <= zari_block:
            break
        K -= zari_block
        zari += 1

    sum = 0
    if zari > 1:
        sum = f(str(10 ** (zari - 1) - 1))

    # 온전
    num_full_numbers = (K - 1) // zari

    if num_full_numbers > 0:
        st = 10 ** (zari - 1)
        ed = st + num_full_numbers - 1
        sum += f(str(ed)) - f(str(st - 1))

    last_num_str = str(10 ** (zari - 1) + num_full_numbers)
    remaining_len = (K - 1) % zari + 1

    for i in range(remaining_len):
        sum += int(last_num_str[i])

    print(sum)


memo["0"] = 0

T = II()
for _ in range(T):
    solve()
