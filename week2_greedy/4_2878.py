import sys

input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
needs = []
for _ in range(N):
    needs.append(int(input()))
needs.sort()

while M > 0:
    to_give = needs[-1] - needs[-2]
    if M >= to_give:
        pass


res = 0
for need in needs:
    res += need**2

print(res)
