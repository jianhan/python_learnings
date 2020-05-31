"""Item 27: Use Comprehensions Instead of map
and filter"""

"""Things to Remember
✦ List comprehensions are clearer than the map and filter built-in
functions because they don’t require lambda expressions.
✦ List comprehensions allow you to easily skip items from the input
list , a behavior that map doesn’t support without help from filter .
✦ Dictionaries and sets may also be created using comprehensions."""

# listcomp is more readable and it is a preferred way over
# map and filter, for instance: square every number in a list

ll = list(range(1, 10))
square = []
for l in ll:
    square.append(l ** 2)
print(square)

squares = [x ** 2 for x in ll]
print(squares)

"""Unlike map , list comprehensions let you easily filter items from the
input list , removing corresponding outputs from the result"""
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

"""The filter built-in function can be used along with map to achieve the
same outcome, but it is much harder to read:"""
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

"""Dictionaries and sets have their own equivalents of list comprehen-
sions (called dictionary comprehensions and set comprehensions,
respectively). These make it easy to create other types of derivative
data structures when writing algorithms:"""
even_squares_dict = {x: x ** 2 for x in a if x % 2 == 0}
threes_cubed_set = {x ** 3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)
