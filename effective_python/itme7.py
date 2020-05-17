""" for loop list, without accessing index """
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(flavor)

""" for loop need access index """
""" This looks clumsy compared with the other examples of iterating over
flavor_list or range . I have to get the length of the list . I have to
index into the array. The multiple steps make it harder to read. """
for i in range(len(flavor_list)):
    print(f'{flavor_list[i]}')

""" Python provides the enumerate built-in function to address this situa-
tion. enumerate wraps any iterator with a lazy generator, enumerate yields
pairs of the loop index and the next value from the given iterator """
it = enumerate(flavor_list)
print(next(it))
print(next(it))

""" unpacking version of loop """
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')
