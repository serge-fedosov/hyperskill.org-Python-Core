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


def task2():
    number = random.randint(11, 29)
    result = number * number

    print(number)
    result2 = 0
    while True:
        try:
            result2 = int(input())
            break
        except ValueError:
            print("Wrong format! Try again.")

    if result == result2:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def select_level():
    level = 0
    while True:
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

        try:
            level = int(input())
            if 1 <= level <= 2:
                break

            print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    return level


task_level = select_level()
correct_answers = 0
for i in range(5):
    if task_level == 1:
        correct_answers += task()
    else:
        correct_answers += task2()

print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
need_save = input()
if need_save in ["yes", "YES", "y", "Yes"]:
    print("What is your name?")
    name = input()
    file = open('results.txt', 'a', encoding='utf-8')
    if task_level == 1:
        file.write(f'{name}: {correct_answers}/5 in level {task_level} (simple operations with numbers 2-9)')
    else:
        file.write(f'{name}: {correct_answers}/5 in level {task_level} (integral squares 11-29)')
    file.close()
    print('The results are saved in "results.txt".')
