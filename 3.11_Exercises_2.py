h = input('Enter Hours: ')
r = input('Enter Rate: ')

try:
    hours = float(h)
    rate = float(r)

    if hours <= 40:
        x = hours * rate
        print('Regular Rate: ' + str(x))
    else:
        x = hours * (rate * 1.5)
        print('Special Rate: ' + str(x))
except:
    print('Error, please enter numeric input.')
