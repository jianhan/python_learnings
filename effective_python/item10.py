fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}


def make_lemonade(count):
    print(count)


def out_of_stock():
    print("out of stock")


""" normally we fetch something and check if that is valid or not
if it is valid then do something else do something else, like following"""
count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

"""with walrus operator we can get & check the variable in one line:"""
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

"""compare this"""
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
to_enjoy = make_smoothies(pieces)
else:
count = fresh_fruit.get('apple', 0)
if count >= 4:
    to_enjoy = make_cider(count)
else:
    count = fresh_fruit.get('lemon', 0)
if count:
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

"""to this """
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('lemon', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'
