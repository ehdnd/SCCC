str = input()

a = list(str)
a.sort(reverse=True)
str = "".join(a)

print(str)
