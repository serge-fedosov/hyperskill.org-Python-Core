def check_name(var):
    if var in ['l', 'O', 'I']:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif var.islower():
        print("It is a common variable")
    elif var.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
