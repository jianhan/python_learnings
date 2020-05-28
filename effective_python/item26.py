"""Item 26: Define Function Decorators with
functools.wraps"""
from functools import wraps

"""Things to Remember
✦ Decorators in Python are syntax to allow one function to modify
another function at runtime.
✦ Using decorators can cause strange behaviors in tools that do intro-
spection, such as debuggers.
✦ Use the wraps decorator from the functools built-in module when
you define your own decorators to avoid issues."""

"""Python has special syntax for decorators that can be applied to
functions. A decorator has the ability to run additional code before
and after each call to a function it wraps. This means decorators
can access and modify input arguments, return values, and raised
exceptions. This functionality can be useful for enforcing semantics,
debugging, registering functions, and more"""


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result

    return wrapper


@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(4)

"""Problem: The value
returned by the decorator—the function that’s called above—doesn’t
think it’s named fibonacci :"""
print(fibonacci)

"""The solution is to use the wraps helper function from the functools
built-in module"""


def trace1(func):
    @wraps(func)
    def wrapper1(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result

    return wrapper1


@trace1
def fibonacci1(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci1(n - 2) + fibonacci1(n - 1)


help(fibonacci1)
