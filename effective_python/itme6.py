""" Tuple and unpacking """
sample_tuple = (1, 2, 3)

print(sample_tuple, sample_tuple[0])

""" key value pair tuple """
food = {'port': 10, 'fish': 20, 'beef': 30, 'kfc': {'price': 12, 'meal': '3 piecebox'}}
food_tuple = tuple(food.items())
print(food_tuple)

""" unpacking from tuple """
item = ('Peanut butter', 'Jelly')
first, second = item  # Unpacking
print(first, 'and', second)

""" swap """


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


# Swap
names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

""" unpack in loop """

# traditional way, the range way
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i + 1}: {name} has {calories} calories')

# unpacking way of doing, this is an ideal way
""" This is the Pythonic way to write this type of loop; it’s short and easy to
understand. There’s usually no need to access anything using indexes. """
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')

"""Using unpacking wisely will enable you to avoid indexing when possi-
ble, resulting in clearer and more Pythonic code."""
