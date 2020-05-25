"""Item 24: Use None and Docstrings to Specify Dynamic
Default Arguments"""

"""Things to Remember
✦ A default argument value is evaluated only once: during function
definition at module load time. This can cause odd behaviors for
dynamic values (like {} , [] , or datetime.now() ).
✦ Use None as the default value for any keyword argument that has a
dynamic value. Document the actual default behavior in the func-
tion’s docstring.
✦ Using None to represent keyword argument default values also
works correctly with type annotations
"""

"""Use case 1 to illustrate the problem: function parameter default value as dynamic: """
import json
from datetime import datetime
from time import sleep
from typing import Optional


def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('Hi there!')
sleep(0.1)
log('Hello again!')

# the output timestamp is exactly the same, this is because the default
# value datetime.now() only execute once upon app start up

"""Solution provide default value as None"""


def log_with_none(message, when=None):
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log_with_none('log_with_none Hi there!')
sleep(0.1)
log_with_none('log_with_none Hello again!')

"""Use case 2: when default value are mutable, this can lead to
strange and unexpected behavior"""


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

"""this is because foo and bar are both equal to the default parameter. They
are the same dictionary object:"""

assert foo is bar

"""Solution:"""


def decode_with_none(data, default=None):
    """Load JSON data from a string.
    Args:
    data: JSON data to decode.
    default: Value to return if decoding fails.
    Defaults to an empty dictionary.
    """

    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode_with_none('bad data')
foo['stuff'] = 5
bar = decode_with_none('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
assert foo is not bar

"""This approach also works with type annotations"""


def log_typed(message: str,
              when: Optional[datetime] = None) -> None:
    """Log a message with a timestamp.
    Args:
    message: Message to print.
    when: datetime of when the message occurred.
    Defaults to the present time.
    """

    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log_typed("test")
sleep(0.1)
log_typed("test after sleep")


# TEST

def dumb_func(msg: str, return_val: list = []) -> list:
    if msg == '':
        msg = "default_val"
    return_val.append(msg)
    return return_val


list1 = dumb_func("test1")

list2 = dumb_func("test2")

print(list1, list2)
