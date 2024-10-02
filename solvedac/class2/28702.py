import sys

input = lambda: sys.stdin.readline().rstrip()
arr = []
for i in range(3):
    arr.append(input())

for i in range(3):
    res = 0
    if arr[i].isdigit():
        res = int(arr[i]) + 3 - i
        break

if res % 15 == 0:
    print("FizzBuzz")
elif res % 5 == 0:
    print("Buzz")
elif res % 3 == 0:
    print("Fizz")
else:
    print(res)
