def to_upper(function):
    def wrapper(args_for_function):
        string = function(args_for_function)
        return string.upper()

    return wrapper
