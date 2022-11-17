n = int(input())

def even():
    b = 0
    while b < n:
        yield b * 2
        b += 1

for i in even():
    print(i)
