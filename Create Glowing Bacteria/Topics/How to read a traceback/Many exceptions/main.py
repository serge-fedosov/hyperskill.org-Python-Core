import math

def find_sqrt(number):
    try:
        print(math.sqrt(number))
    except TypeError:
        try:
            print(math.sqrt(int(number)))
        except Exception:
            print('Please pass a number like "5" or 5')
