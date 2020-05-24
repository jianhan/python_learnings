"""Item 21: Know How Closures Interact with
Variable Scope"""

"""Things to Remember
✦ Closure functions can refer to variables from any of the scopes in
which they were defined.
✦ By default, closures can’t affect enclosing scopes by assigning
variables.
✦ Use the nonlocal statement to indicate when a closure can modify a
variable in its enclosing scopes.
✦ Avoid using nonlocal statements for anything beyond simple
functions."""

"""sort a list of numbers but prioritize one group of
numbers to come first. This pattern is useful when you’re rendering a
user interface and want important messages or exceptional events to
be displayed before everything else."""


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

"""It’d be nice if this function returned whether higher-priority items
were seen at all so the user interface code can act accordingly"""


def sort_priority2(numbers, group):
    found = False  # Scope: 'sort_priority2'

    def helper(x):
        if x in group:
            found = True  # Scope: 'helper' -- Bad!
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)

"""How did python interpreter find variable scope"""

"""When you reference a variable in an expression, the Python interpreter
traverses the scope to resolve the reference in this order:
1. The current function’s scope.
2. Any enclosing scopes (such as other containing functions).
3. The scope of the module that contains the code (also called the
global scope).
4. The built-in scope (that contains functions like len and str )."""

"""Assigning variable works differently: If the variable is
already defined in the current scope, it will just take on the new
value. If the variable doesn’t exist in the current scope, Python treats
the assignment as a variable definition
"""

"""The nonlocal statement is used to indicate that scope traversal should
happen upon assignment for a specific variable name. The only limit
is that nonlocal won’t traverse up to the module-level scope"""


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found  # Added

        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found
