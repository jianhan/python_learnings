def to_upper(s) -> str:
    return s.upper()


name = "jim"
# use listcomp is more readable and not change
# the original value.
uppser_letters = [to_upper(s) for s in name]
print(uppser_letters, name)
# [J,I,M]

"""Filter , Map and Lambda"""

person = [{'name': 'Jim', 'age': 12}, {'name': 'Jack', 'age': 13}, {'name': 'Smith', 'age': 14},
          {'name': 'Andy', 'age': 15}]

# to get all person that is age is greater than or equals to 13
person_filtered = list(filter(lambda p: p['age'] >= 13, person))
print(person_filtered)

