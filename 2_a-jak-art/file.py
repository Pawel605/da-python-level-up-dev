from collections import namedtuple
from functools import wraps


# task 2.1
def greeter(func):
    def inner(*args):
        return "Aloha " + func(*args).title()
    return inner


# task 2.2
def sums_of_str_elements_are_equal(func):
    def wrapper(*args, **kwargs):
        number_list = func(*args, **kwargs).split()
        first_number = second_number = 0

        for n in number_list[0]:
            if n != "-":
                first_number += int(n)
        if number_list[0][0] == "-":
            first_number *= -1

        for n in number_list[1]:
            if n != "-":
                second_number += int(n)
        if number_list[1][0] == "-":
            second_number *= -1

        if first_number == second_number:
            return str(first_number) + " == " + str(second_number)
        else:
            return str(first_number) + " != " + str(second_number)
    return wrapper


# task 2.3
def format_output(*required_keys):
    def decorator(func):
        @wraps(func)
        def wrapper(*wrapper_args):
            Argument = namedtuple("Argument", ["original", "split"])
            arguments = [Argument(arg, str.split(arg, sep='__'))
                         for arg in required_keys]
            func_dict = func(*wrapper_args)
            result_dict = {}
            validated_arguments = [arg in func_dict for seq in arguments for arg in seq.split]
            if not all(validated_arguments):
                raise ValueError
            for arg in arguments:
                result_dict[arg.original] = " ".join(["Empty value" if func_dict[x] == '' else func_dict[x] for x in arg.split])
            return result_dict

        return wrapper

    return decorator


# task 2.4
def add_method_to_instance(klass):
    def decorator(func):
        @classmethod
        @wraps(func)
        def wrapper(self):
            return func()
        setattr(klass, func.__name__, wrapper)

        return func

    return decorator
