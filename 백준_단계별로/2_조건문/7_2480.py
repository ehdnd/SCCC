A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + (A*1000))
elif A > B > C or A > C > B:
    print(A*100)
elif B > A > C or B > C > A:
    print(B*100)
elif C > A > B or C > B > A:
    print(C*100)
else:
    if A == B:
        print(1000 + (A*100))
    elif A == C:
        print(1000 + (A*100))
    else:
        print(1000 + (B*100))

# # max 함수?
# a,b,c=map(int,input().split())
# if a==b==c:
#     print(10000+a*1000)
# elif a==b or b==c:
#     print(1000+b*100)
# elif a==c:
#     print(1000+a*100)
# else:
#     print(max(a,b,c)*100)