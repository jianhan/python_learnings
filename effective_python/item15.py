from collections.abc import MutableMapping

"""Things to Remember
✦ Since Python 3.7, you can rely on the fact that iterating a dict
instance’s contents will occur in the same order in which the keys
were initially added.
✦ Python makes it easy to define objects that act like dictionaries but
that aren’t dict instances. For these types, you can’t assume that
insertion ordering will be preserved.
✦ There are three ways to be careful about dictionary-like classes:
Write code that doesn’t rely on insertion ordering, explicitly check
for the dict type at runtime, or require dict values using type anno-
tations and static analysis."""

"""Item 15: Be Cautious When Relying on dict Insertion
Ordering"""


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


"""In Python 3.5 and before, iterating over a dict would return keys in
arbitrary order"""
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
print(baby_names)

"""This happened because the dictionary type previously implemented
its hash table algorithm with a combination of the hash built-in func-
tion and a random seed that was assigned when the Python inter-
preter started. Together, these behaviors caused dictionary orderings
to not match insertion order and to randomly shuffle between pro-
gram executions."""

"""Starting with Python 3.6, and officially part of the Python specifica-
tion in version 3.7, dictionaries will preserve insertion order"""


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


my_func(goose='gosling', kangaroo='joey')

"""The way that dictionaries preserve insertion ordering is now part of
the Python language specification. For the language features above,
you can rely on this behavior and even make it part of the APIs you
design for your classes and functions."""

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

"""use the
collections.abc built-in module to define a new dictionary-like class
that iterates its contents in alphabetical order"""

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)
