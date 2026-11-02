import inspect


def trace_recursion(func):
    
    def wrapper(*args, **kwargs):
        depth = 0
        for frame in inspect.stack(context=0):
            if frame.frame.f_code is func.__code__:
                depth += 1
        indent = "    " * depth
        print(f"{indent}Вызов {func.__name__}: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{indent}Возврат {func.__name__}: {result}")
        return result
    
    return wrapper