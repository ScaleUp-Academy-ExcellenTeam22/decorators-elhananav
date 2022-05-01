from functools import wraps


def type_check(correct_type):
    """
    The factory should take one argument, a type, and then returns a decorator that
    the checks if the parameter the function receives is of the correct type. If it is wrong,
    it should raise a custom error.
    :param correct_type: Type to check.
    :return: The function.
    """
    @wraps(correct_type)
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args):
            if not isinstance(func(*args), correct_type):
                raise TypeError
            return func(*args)
        return inner_wrapper
    return wrapper


if __name__ == "__main__":
    @type_check(str)
    def times2(num):
        return num * 2
