# H, M = map(int, input().split())

# if M >= 45:
#     print(f"{H} {M}")
# elif H == 0:
#     print(f"23 {M+15}")
# else:
#     print(f"{H-1} {M+15}")

H, M = map(int, input().split())

if M >= 45:
    print(f"{H} {M-45}")
elif H == 0:
    print(f"23 {M+15}")
else:
    print(f"{H-1} {M+15}")