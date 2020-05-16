""" List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the
items in a list do not need to be of the same type. """

sample = ["one", "two", "three", "four"]
# when slice, the beginging part is inclusive, the ending part is not
print("a[2] = ", sample[2])
# ["one", "two", "three"]
print("a[0:3] = ", sample[0:3])
# ["three"]
print("a[5:] = ", sample[2:3])

# append
# ["one", "two", "three", "four"]
sample.append("five")
print(sample)

# insert, when insert in an index, it will shift
# entire list to the right hand side
# ["new one", "one", "two", "three", "four"]
sample.insert(0, "new one")
print(sample)

# if the index inserting is exceed max index, it just
# insert at the end
sample.insert(10, "new 10")
print(sample)

# likewise for the negative value, it will
# insert in the begning of the list
sample.insert(-10, "minus new 10")
print(sample)

# delete list
del sample[0]
print(sample)

# if delete from an index is not valid, then
# it will throw error: IndexError: list assignment index out of range
del sample[0]
print(sample)

# use pop to delete it
first = sample.pop(0)
print(first)

""" difference between pop and delete, when use pop, it removes from list and
returns the value, del do not, so if you want to pop it out and use it somewhere else
then use pop, if you just want to delete it and be done, then use del """

# dupe list
dupe_sample = ["one", "one", "two", "two", "three"]
print(dupe_sample)

# delete by value, NOTICE: it will only delete the first one it can find
# in this example the output of list still
# ["one", "two", "two"...], as it shown, the value one still exists in list
dupe_sample.remove("one")
print(dupe_sample)

"""list in function are passed by reference
"""

ns = [1, 2, 3]


def add_first(ll):
    ll[0] = ll[0] + 1


add_first(ns)

print(ns)

""" copy list """
my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods will not work
friend_foods = my_foods[:]
friend_foods.append('cherry')

print(my_foods, friend_foods)

# wrong way of copy list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
friend_foods.append('cherry')

print(my_foods, friend_foods)

