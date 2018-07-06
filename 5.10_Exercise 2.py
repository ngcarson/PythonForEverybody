from pip._vendor.distlib.compat import raw_input

largest = None
smallest = None

while True:
    try:
        num = raw_input("Enter a number: ")
        if num != 'done' :
            n = int(num)
            if largest == None or largest < n :
                largest = n
            if smallest == None or smallest > n :
                smallest = n
        else:
            break
        print("Maximum is", largest)
        print("Minimum is", smallest)
    except:
        print("Invalid input")
