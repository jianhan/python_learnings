""" the most common way of formatting string """
a = 0b10111011
b = 0xc5f
print('Binary is %d , hex is %d ' % (a, b))

""" Problem 1, it is not easy to change, must make sure left hand side and right hand side in sync at all time,
otherwise it will error out."""
key = 'my_var'
value = 1.234
# following will fail
# reordered_string = '%.2f = %-10s' % (key, value)

""" Problem 2, hard to read """
pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

""" Problem 3, if the same string appear multiply times, it has to be repeated """
template = '%s loves food. See %s cook.'
name = 'Max'
formatted = template % (name, name)
print(formatted)

""" Solution 1, using dict and named parameter """
name = 'Max'
template = '%s loves food. See %s cook.'
before = template % (name, name)
# Tuple
template = '%(name)s loves food. See %(name)s cook.'
after = template % {'name': name}  # Dictionary
assert before == after

""" Problem for solution 1: duplication and verbose """
# soup repeated 3 times as following
soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)

""" redundency example 2 """
menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entrée is %(special)s.')
formatted = template % menu
print(formatted)

""" a better way of doing it The format Built-in and str.format
Python 3 added support for advanced string formatting that is more
expressive than the old C-style format strings that use the % operator.
For individual Python values, this new functionality can be accessed
through the format built-in function """

a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

""" You can use this functionality to format multiple values together
by calling the new format method of the str type. """
key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

formatted = '{0} loves food. See {0} cook.'.format(name)
print(formatted)

name = ["bob", "jake"]
e = enumerate(name)
print(f'name is {e}')

""" all different styles """
f_string = f'{key:<10} = {value:.2f}'
c_tuple = '%-10s = %.2f' % (key, value)
str_args = '{:<10} = {:.2f}'.format(key, value)
str_kw = '{key:<10} = {value:.2f}'.format(key=key,
                                          value=value)
c_dict = '%(key)-10s = %(value).2f' % {'key': key,
                                       'value': value}

""" example that is remove duplication """
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))
new_style = '#{}: {:<10s} = {}'.format(
    i + 1,
    item.title(),
    round(count))
f_string = f'#{i + 1}: {item.title():<10s} = {round(count)}'
assert old_style == new_style == f_string
