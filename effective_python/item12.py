"""Things to Remember
✦ Specifying start, end, and stride in a slice can be extremely
confusing.
✦ Prefer using positive stride values in slices without start or end
indexes. Avoid negative stride values if possible.
✦ Avoid using start, end, and stride together in a single slice. If you
need all three parameters, consider doing two assignments (one
to stride and another to slice) or using islice from the itertools
built-in module."""

"""Python has special syntax for the stride of a slice in
the form somelist[start:end:stride] . This lets you take every nth item
when slicing a sequence"""

x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

"""The problem is that the stride syntax often causes unexpected behav-
ior that can introduce bugs. For example, a common Python trick for
reversing a byte string is to slice the string with a stride of -1"""
x = b'mongoose'
y = x[::-1]
print(y)

x = '寿司'
y = x[::-1]
print(y)

"""But it will break when Unicode data is encoded as a UTF-8 byte string:"""
w = '寿司'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
print(z)

"""I suggest you avoid using a stride along with
start and end indexes. If you must use a stride, prefer making it a
positive value and omit start and end indexes. If you must use a stride
with start or end indexes, consider using one assignment for striding
and another for slicing:"""
y = x[::2]  # ['a', 'c', 'e', 'g']
z = y[1:-1]  # ['c', 'e']
