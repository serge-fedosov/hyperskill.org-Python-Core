from collections import deque

stack = deque()
n = int(input())
for _ in range(n):
    operation, *name = input().split(" ", 1)
    if operation == "PUSH":
        stack.append(name[0])
    else:
        stack.pop()

for _ in range(len(stack)):
    print(stack.pop())
