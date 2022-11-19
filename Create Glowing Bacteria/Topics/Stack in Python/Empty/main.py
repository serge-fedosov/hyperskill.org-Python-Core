from collections import deque

# please don't change the following line
candy_bag = deque(input().split())

# your code here
n = int(input())
for _ in range(n):
    operation, *name = input().split(" ", 1)
    if operation == "PUT":
        candy_bag.append(name[0])
    else:
        if len(candy_bag) == 0:
            print("We are out of candies :(")
        else:
            print(candy_bag.pop())
