def check_integer(num):
    if not 45 < num < 67:
        raise NotInBoundsError
    else:
        return num


def error_handling(num):
    try:
        result = check_integer(num)
        print(result)
    except NotInBoundsError as err:
        print(err)
