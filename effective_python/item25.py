"""Item 25: Enforce Clarity with Keyword-Only and
Positional-Only Arguments"""

"""Things to Remember
✦ Keyword-only arguments force callers to supply certain arguments
by keyword (instead of by position), which makes the intention of a
function call clearer. Keyword-only arguments are defined after a
single * in the argument list.
✦ Positional-only arguments ensure that callers can’t supply
certain parameters using keywords, which helps reduce coupling.
Positional-only arguments are defined before a single / in the argu-
ment list.
✦ Parameters between the / and * characters in the argument list
may be supplied by position or keyword, which is the default for
Python parameters."""


# Considering the function below
def safe_division(number, divisor,
                  ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# when using it, it is straight forward however, from caller's
# perspective it may be a bit confusing since the last 2 parameters
# both boolean, caller do not know which one represent what
result = safe_division(1.0, 10 ** 500, True, False)
print(result)

result = safe_division(1.0, 0, False, True)
print(result)

"""Improvement 1: use default parameters"""


def safe_division_b(number, divisor,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


"""Then, callers can use keyword arguments to specify which of the
ignore flags they want to set for specific operations, overriding the
default behavior:"""
result = safe_division_b(1.0, 10 ** 500, ignore_overflow=True)
print(result)

result = safe_division_b(1.0, 0, ignore_zero_division=True)
print(result)

"""The problem is caller still have the same issue: confusion"""
assert safe_division_b(1.0, 10 ** 500, True, False) == 0

"""With complex functions like this, it’s better to require that callers are
clear about their intentions by defining functions with keyword-only
arguments."""


# we can define a function force usres to call the function with keyword-only
# style The * symbol in the argument list indicates the end
# of positional arguments and the beginning of keyword-only
# arguments

def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# default parameter values still works
result = safe_division_c(1.0, 0, ignore_zero_division=True)
assert result == float('inf')

try:
    result = safe_division_c(1.0, 0)
except ZeroDivisionError:
    pass  # Expected

# problem: Callers may specify the first two required arguments
# ( number and divisor ) with a mix of positions and keywords
assert safe_division_c(number=2, divisor=5) == 0.4
assert safe_division_c(divisor=5, number=2) == 0.4
assert safe_division_c(2, divisor=5) == 0.4


# Python 3.8 positional-only
# arguments. These arguments can be supplied only by position and
# never by keyword
# The / symbol in the
# argument list indicates where positional-only arguments end
def safe_division_d(numerator, denominator, /, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return numerator / denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


assert safe_division_d(2, 5) == 0.4

# if calling by keywords, then it will generate error
safe_division_d(numerator=2, denominator=5)
