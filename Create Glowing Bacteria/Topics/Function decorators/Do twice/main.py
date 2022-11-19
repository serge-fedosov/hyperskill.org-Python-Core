def do_twice(function):
    def wrapper(args_for_function):
        function(args_for_function)
        function(args_for_function)

    return wrapper
