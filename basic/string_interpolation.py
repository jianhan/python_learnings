from string import Template

"""
1. %-format method is very old method for interpolation and is not recommended to use as it decrease the code readability.
2. In str.format() method we pass the string object to the format() function for string interpolation.
3. In template method we make a template by importing template class from built in string module.
4. Literal String Interpolation method is powerful interpolation method which is easy to use and increase the code readability.
"""

""" f-strings: It provides access to embedded Python expressions inside string constants. """
name = "jim"
age = 12
print(f'Hello my name is {name} and I am {age}')

a = 12
b = 13
print(f'{a * b}')

print("%s %s %d" % ("Jim", "Smith", 12))

name = 'world'
program = 'python'
print('Hello %s! This is %s.' % (name, program))

name = 'world'
print('hello {}'.format(name))

name = 'world'
program = 'python'
print('Hello {name}!This is {program}.'.format(name=name, program=program))

name = 'world'
program = 'python'
new = Template('Hello $name! This is $program.')
print(new.substitute(name=name, program=program))
