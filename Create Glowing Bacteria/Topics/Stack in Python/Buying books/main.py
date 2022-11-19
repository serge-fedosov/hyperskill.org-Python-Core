from collections import deque

stack = deque()
n = int(input())

for _ in range(n):
    operation, *book = input().split(" ", 1)
    if operation == "BUY":
        stack.append(book[0])
    else:
        print(stack.pop())
