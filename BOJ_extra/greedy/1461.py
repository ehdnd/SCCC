import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
books = list(map(int, input().split()))

plus_books = []
minus_books = []

for book in books:
    if book > 0:
        plus_books.append(book)
    else:
        minus_books.append(abs(book))

plus_books.sort(reverse=True)
minus_books.sort(reverse=True)

move = 0
for i in range(0, len(plus_books), M):
    move += plus_books[i] * 2

for i in range(0, len(minus_books), M):
    move += minus_books[i] * 2

move -= abs(max(books, key=lambda x: abs(x)))

print(move)
