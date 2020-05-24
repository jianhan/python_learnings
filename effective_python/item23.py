"""Item 23: Provide Optional Behavior with
Keyword Arguments"""

"""Things to Remember
✦ Function arguments can be specified by position or by keyword.
✦ Keywords make it clear what the purpose of each argument is when
it would be confusing with only positional arguments.
✦ Keyword arguments with default values make it easy to add new
behaviors to a function without needing to migrate all existing
callers.
✦ Optional keyword arguments should always be passed by keyword
instead of by position.
"""

"""in Python you may pass
arguments by position when calling a function"""


def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6

"""These calls are equivalent"""
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

"""Using dict to pass to function's parameters"""
my_kwargs = {
    'number': 20,
    'divisor': 7,
}
assert remainder(**my_kwargs) == 6

"""mix the ** operator with positional arguments or keyword
arguments in the function call, as long as no argument is repeated:"""
my_kwargs = {
    'divisor': 7,
}
assert remainder(number=20, **my_kwargs) == 6

"""use the ** operator multiple times if you know that the
dictionaries don’t contain overlapping keys"""
my_kwargs = {
    'number': 20,
}
other_kwargs = {
    'divisor': 7,
}
assert remainder(**my_kwargs, **other_kwargs) == 6

"""A function with any number of parameters:"""


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


print_parameters(alpha=1.5, beta=9, gamma=4)

"""default parameter value"""


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg per second')


def flow_rate_period(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_per_second = flow_rate_period(weight_diff, time_diff)
flow_per_hour = flow_rate_period(weight_diff, time_diff, period=3600)
