a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two: ', a[3:5])
print('All but ends:', a[1:7])

"""When slicing from the start of a list , you should leave out the zero
index to reduce visual noise:"""
assert a[:5] == a[0:5]

"""When slicing to the end of a list , you should leave out the final index
because it’s redundant"""
assert a[5:] == a[5:len(a)]

"""example: """
ll = list(range(0, 9))
print(ll[4: 5])
print(ll[:])  # entire list
print(ll[:5])  # first 5 elements inclusive, [0,1,2,3,4]
print(ll[:-1])  # when negative, it operate from right hand side, in this case
# the starting is index 0, the ending is 1 from right to left, therefore
# it would print [0,1,2,3,4,5,6,7]
print(ll[4:])  # print [4, 5, 6 , 7 ,8]
print(ll[2: -1])  # print [2,3,4,5,6,7]
print(ll[-3: -1])  # print [6,7]

"""slice assignment will not change the original list"""
print("before new_ll = ll[1:2]: ll is -", ll)
new_ll = ll[1:2]
print("after new_ll = ll[1:2]: ll is -", ll)
print("new ll is -", new_ll)

