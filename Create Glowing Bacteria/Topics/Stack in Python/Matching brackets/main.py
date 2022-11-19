from collections import deque

expression = input()

stack = deque()
error = False
for w in expression:
    if w == '(':
        stack.append('(')
    elif w == ')':
        if len(stack) == 0:
            error = True
            break
        stack.pop()


if not error and len(stack) == 0:
    print("OK")
else:
    print("ERROR")
