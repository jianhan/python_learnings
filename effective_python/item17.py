"""Item 17: Prefer defaultdict Over setdefault to
Handle Missing Items in Internal State"""

"""Things to Remember
✦ If you’re creating a dictionary to manage an arbitrary set of poten-
tial keys, then you should prefer using a defaultdict instance from
the collections built-in module if it suits your problem.
✦ If a dictionary of arbitrary keys is passed to you, and you don’t con-
trol its creation, then you should prefer the get method to access its
items. However, it’s worth considering using the setdefault method
for the few situations in which it leads to shorter code."""

from collections import defaultdict

"""for some use cases setdefault appears to be the
shortest option"""

visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}
visits.setdefault('France', set()).add('Arles')  # Short
# if (japan := visits.get('Japan')) is None:
#     visits['Japan'] = japan = set()
# japan.add('Kyoto')  # Long
# print(visits)

"""When we control over how item should be created within dict, then"""


class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)

"""However, setdefault still a bit confusion: best solution as following:"""


class Visits2:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits2 = Visits2()
visits2.add('England', 'Bath')
visits2.add('England', 'London')
print(visits2.data)
