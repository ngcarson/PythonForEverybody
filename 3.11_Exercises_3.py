s = input('Enter score: ')

try:
    score = float(s)

    if score == 10:
        print('Perfect score')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('Bad score')
except:
    print('Error, please enter numeric input.')
