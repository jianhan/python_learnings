"""Things to Remember
✦ Unpacking assignments may use a starred expression to catch all
values that weren’t assigned to the other parts of the unpacking
pattern into a list .
✦ Starred expressions may appear in any position, and they will
always become a list containing the zero or more values they
receive.
✦ When dividing a list into non-overlapping pieces, catch-all unpack-
ing is much less error prone than slicing and indexing."""

"""Item 13: Prefer Catch-All Unpacking Over Slicing"""

"""Python also supports catch-all
unpacking through a starred expression. This syntax allows one part
of the unpacking assignment to receive all values that didn’t match
any other part of the unpacking pattern."""

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)

"""with the addition of starred expressions, the value of unpack-
ing iterators becomes clear. For example"""


def gen_csv():
    yield 'Name', 'Age'
    yield 'Jim', '12'
    yield 'Tom', '13'


all_csv_rows = list(gen_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header:', header)
print('Row count: ', len(rows))

"""Unpacking with a starred expression makes it easy to process the first
row—the header—separately from the rest of the iterator’s contents.
This is much clearer"""

header, *rows = gen_csv()
print('CSV Header:', header)
print('Row count: ', len(rows))

di = {"name": "Jim", "age": 12}
name, age = di
print(name, '---', age)
