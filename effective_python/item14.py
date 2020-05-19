"""✦ The sort method of the list type can be used to rearrange a list’s
contents by the natural ordering of built-in types like strings, inte-
gers, tuples, and so on.
✦ The sort method doesn’t work for objects unless they define a natu-
ral ordering using special methods, which is uncommon.
✦ The key parameter of the sort method can be used to supply a
helper function that returns the value to use for sorting in place of
each item from the list .
✦ Returning a tuple from the key function allows you to combine mul-
tiple sorting criteria together. The unary minus operator can be
used to reverse individual sort orders for types that allow it.
✦ For types that can’t be negated, you can combine many sorting cri-
teria together by calling the sort method multiple times using dif-
ferent key functions and reverse values, in the order of lowest rank
sort call to highest rank sort call"""

"""Item 14: Sort by Complex Criteria Using the key
Parameter"""

"""By default, sort will
order a list ’s contents by the natural ascending order of the items."""
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

"""The sort method works for nearly all built-in types (strings, floats,
etc.) that have a natural ordering to them"""


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


"""Sorting objects of this type doesn’t work because the sort method
tries to call comparison special methods that aren’t defined by the
class"""
tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]
# this will fail
# tools.sort()

"""Often there’s an attribute on the object that you’d like to use for sort-
ing. To support this use case, the sort method accepts a key param-
eter that’s expected to be a function. The key function is passed a
single argument, which is an item from the list that is being sorted."""
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted: ', tools)

tools.sort(key=lambda x: x.weight)
print('By weight:', tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case sensitive: ', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places)

"""multiple criteria for sorting: SOlution 1: TUPLE"""
"""Tuples are compara-
ble by default and have a natural ordering, meaning that they imple-
ment all of the special methods, such as __lt__ , that are required by
the sort method"""

power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw)  # Matches expectations

drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]  # Same weight
assert drill[1] < sander[1]  # Alphabetically less
assert drill < sander  # Thus, drill comes first

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

"""Limitation: all sort direction must be the same: One limitation of having the key function return a tuple is that the
direction of sorting for all criteria must be the same (either all in
ascending order, or all in descending order). If I provide the reverse
parameter to the sort method, it will affect both criteria in the tuple
the same way"""
power_tools.sort(key=lambda x: (x.weight, x.name),
                 reverse=True)  # Makes all criteria descending
print(power_tools)

"""For numerical values it’s possible to mix sorting directions by using
the unary minus operator in the key function"""
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)
"""Unfortunately, unary negation isn’t possible for all types."""

"""For situations like this, Python provides a stable sorting algorithm.
The sort method of the list type will preserve the order of the input
list when the key function returns values that are equal to each
other."""
power_tools.sort(key=lambda x: x.name)
# Name ascending
power_tools.sort(key=lambda x: x.weight,  # Weight descending
                 reverse=True)
print(power_tools)
