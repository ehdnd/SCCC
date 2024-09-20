# A, B = map(int, input().split())
# C = int(input())

# m = B + C
# h = m // 60

# totalH = h + A
# totalM = m - (60 * h)

# if totalH != 24:
#     if totalM != 60:
#         print(totalH, totalM)
#     else:
#         print(totalH, 0)
# else:
#     if totalM !=60:
#         print(0, totalM)
#     else:
#         print(0, 0)

A, B = map(int, input().split())
C = int(input())

m = B + C
h = m // 60

totalH = h + A
totalM = m % 60

if totalH >= 24:
    print(totalH - 24, totalM)
else:
   print(totalH, totalM)