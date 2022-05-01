from functools import wraps


def print_surprise(function):
    """
    :param function: A function which will be changed to print surprise
    :return: The inner function
    """
    @wraps(function)
    def inner(*args):
        print("surprise!")
    return inner
