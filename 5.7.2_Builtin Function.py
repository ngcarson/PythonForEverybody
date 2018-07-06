values = [4, 5, 6, 7, 8, 9]

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    #return smallest
    print(smallest)

min(values)