"""Item 20: Prefer Raising Exceptions to Returning None"""
"""Things to Remember
✦ Functions that return None to indicate special meaning are error
prone because None and other values (e.g., zero, the empty string)
all evaluate to False in conditional expressions.
✦ Raise exceptions to indicate special situations instead of returning
None . Expect the calling code to handle exceptions properly when
they’re documented.
✦ Type annotations can be used to make it clear that a function will
never return the value None , even in special situations.
"""

"""a helper function
that divides one number by another. In the case of dividing by zero,
returning None seems natural because the result is undefined"""


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


"""Following is a valid use case, it actually detected 1 is divided by 0
therefore throw error"""
x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

"""However, when we have a another case which is valid division, still return error, where
it should work normally"""
x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs')  # This runs! But shouldn't

"""better way to reduce these errors is to never return
None for special cases. Instead, raise an Exception up to the caller
and have the caller deal with it."""


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    Raises:
    ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


x, y = 5, 9
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
