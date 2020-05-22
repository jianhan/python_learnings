"""Item 16: Prefer get Over in and KeyError to Handle
Missing Dictionary Keys"""

"""Things to Remember
✦ There are four common ways to detect and handle missing keys
in dictionaries: using in expressions, KeyError exceptions, the get
method, and the setdefault method.
✦ The get method is best for dictionaries that contain basic types
like counters, and it is preferable along with assignment expres-
sions when creating dictionary values has a high cost or may raise
exceptions.
✦ When the setdefault method of dict seems like the best fit for your
problem, you should consider using defaultdict instead."""

"""The three fundamental operations for interacting with dictionar-
ies are accessing, assigning, and deleting keys and their associated
values"""

counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

"""to increse counter, need to 1> check if key exists, 2> increase it, accessing
keys 2 times, assignment statetment once: Traditional way"""
key = 'wheat'
if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1

"""another way: KeyError exception when you try to get the value
for a key that doesn’t exist"""
# This approach is more efficient because it
# requires only one access and one assignment

try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1

"""Another event shorter way: """
key1 = 'corn'
count = counters.get(key1, 0)
counters[key1] = count + 1

print(counters)

"""When list values are complex type:"""
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []
# don’t need to assign it again because the list is modified by
# reference in the later call to append .
names.append(who)
print(votes)

"""More efficient way"""
"""It’s also possible to rely on the KeyError exception being raised when
the dictionary value is a list . This approach requires one key access
if the key is present, or one key access and one assignment if it’s
missing"""
try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

"""THird way: """
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

"""THird way: shorter way, most readable way"""
"""The approach that involves using get to fetch list values can
further be shortened by one line if you use an assignment expres-
sion"""

# only works in python 3.8
# if (names := votes.get(key)) is None:
#     votes[key] = names = []
# names.append(who)

"""Final Way: use setdefault method provided by dict type"""
"""a bit less readable since what we are doing is to get value not set"""
names = votes.setdefault(key, [])
names.append(who)

"""There’s also one important gotcha: The default value passed to
setdefault is assigned directly into the dictionary when the key is
missing instead of being copied"""

data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before:', data)
value.append('hello')
print('After: ', data)

"""this might introduce strange bugs"""
"""try not to use setdefault at all"""
