def tagged(func):
    def wrapper(args_for_function):
        string = func(args_for_function)
        return f"<title>{string}</title>"

    return wrapper
