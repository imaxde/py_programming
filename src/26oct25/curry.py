from inspect import getfullargspec

def curry(function, arg_count):
    original_arguments = getfullargspec(function)
    # т.к. нужно поддерживать только позиционные аргументы, любое отклонение будет вызывать ошибку
    if arg_count != len(original_arguments.args):
        raise Exception("Неверное количество аргументов")
    def help_function(*args):
        if len(args) < arg_count:
            return lambda x: help_function(*args, x)
        return function(*args)
    return help_function

def uncurry(function, arg_count):
    def help_function(*args):
        function_to_call = function
        for argument in args:
            function_to_call = function_to_call(argument)
        return function_to_call
    return help_function