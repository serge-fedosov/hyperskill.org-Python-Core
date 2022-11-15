def check(val):
    if not val.isdigit():
        print("It is not a number!")
        return

    number = int(val)
    if number >= 202:
        print(number)
    else:
        print("There are less than 202 apples! You cheated me!")
