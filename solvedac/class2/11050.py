# math.factorial() 을 사용하자
import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())


def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def jud(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))


print(jud(N, K))
