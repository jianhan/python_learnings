"""Item 8: Use zip to Process Iterators in Parallel"""
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)

uppers = [n.upper() for n in names]
print(uppers)

"""zip wraps two or more iterators with a lazy generator. The zip gener-
ator yields tuples containing the next value from each iterator."""
longest_name = None
max_count = 0
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(max_count)
