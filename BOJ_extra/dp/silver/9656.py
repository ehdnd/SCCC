import sys

input = lambda: sys.stdin.readline().rstrip()


N = int(input())
print("CY") if N % 2 != 0 else print("SK")
