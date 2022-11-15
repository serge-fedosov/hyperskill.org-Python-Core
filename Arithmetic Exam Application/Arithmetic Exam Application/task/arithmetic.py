import random


def task():
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
    result2 = 0
    while True:
        try:
            result2 = int(input())
            break
        except ValueError:
            print("Incorrect format.")

    if result == result2:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


n = 0
for i in range(5):
    n += task()

print(f"Your mark is {n}/5.")
