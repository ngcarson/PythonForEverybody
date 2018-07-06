largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for value in [3, 41, 12, 9, 74, 15]:
    if smallest is None or value < smallest :
        smallest = value
    print(value, smallest)
print('Smallest:', smallest)
