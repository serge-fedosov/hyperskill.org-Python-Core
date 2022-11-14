a, operation, b = input().split(" ")
op1 = int(a)
op2 = int(b)

result = None
if operation == "+":
    result = op1 + op2
elif operation == "*":
    result = op1 * op2
elif operation == "-":
    result = op1 - op2

print(result)
