import random

# a, operation, b = input().split(" ")
# op1 = int(a)
# op2 = int(b)
#
# result = None
# if operation == "+":
#     result = op1 + op2
# elif operation == "*":
#     result = op1 * op2
# elif operation == "-":
#     result = op1 - op2
#
# print(result)

op1 = random.randint(2, 9)
op2 = random.randint(2, 9)
operation = random.randint(1, 3)

result = None
op = ""
if operation == 1:
    op = "+"
    result = op1 + op2
elif operation == 2:
    op = "-"
    result = op1 - op2
elif operation == 3:
    op = "*"
    result = op1 * op2

print(op1, op, op2)
result2 = int(input())

if result == result2:
    print("Right!")
else:
    print("Wrong!")
