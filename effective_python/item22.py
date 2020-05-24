"""Item 22: Reduce Visual Noise with Variable Positional
Arguments"""

"""Things to Remember
✦ Functions can accept a variable number of positional arguments by
using *args in the def statement.
✦ You can use the items from a sequence as the positional arguments
for a function with the * operator.
✦ Using the * operator with a generator may cause a program to run
out of memory and crash.
✦ Adding new positional parameters to functions that accept *args
can introduce hard-to-detect bugs."""

"""Accepting a variable number of positional arguments can make a
function call clearer and reduce visual noise"""


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('test', {'name': 'Jim', 'age': 12})
log('test', [])
log('test', {})

"""Having to pass an empty list when I have no values to log is cum-
bersome and noisy."""


def logOptional(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


logOptional('My numbers are', 1, 2)
logOptional('Hi there')  # Much better

favorites = [7, 33, 99]
logOptional('Favorite colors with *', *favorites)
logOptional('Favorite colors without *', favorites)

"""2 Problems with this kind of function parameters style"""
"""1: if passed a generator, then it will convert to tuple first
so if the generator produces large dataset, it can cause
memory issue"""

"""2: The second issue with *args is that you can’t add new positional
arguments to a function in the future without migrating every caller.
"""


def logNewVer(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')


logNewVer(1, 'Favorites', 7, 33)  # New with *args OK
logNewVer(1, 'Hi there')  # New message only OK
logNewVer('Favorite numbers', 7, 33)  # Old usage breaks
