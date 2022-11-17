n = int(input())


def squares():
    yield i * i


for i in range(1, n + 1):
    print(next(squares()))
