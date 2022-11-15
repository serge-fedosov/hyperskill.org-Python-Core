class NegativeSumError(Exception):
    def __str__(self):
        return "Wrong!"


def sum_with_exceptions(a, b):
    sum_ = a + b
    if sum_ < 0:
        raise NegativeSumError
    else:
        return sum_
