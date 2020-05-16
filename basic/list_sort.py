""" sort that will change the original list """

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# revserse sorting
cars.sort(reverse=True)
print(cars)

""" get sorted varsion of the list but do not change the original list """
sorted_cars = sorted(cars)
print("sorted", sorted_cars, "original", cars)

""" reverse function: it change the order of elements in original list """
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
