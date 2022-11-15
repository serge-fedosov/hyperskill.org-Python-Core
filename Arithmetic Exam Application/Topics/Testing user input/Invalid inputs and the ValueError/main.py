def check():
    try:
        your_int = int(input())
        if 25 <= your_int <= 37:
            print(your_int)
        else:
            print("Correct the error!")
    except ValueError:
        print("Correct the error!")
