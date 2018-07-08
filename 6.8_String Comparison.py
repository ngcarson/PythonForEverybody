# Auto inputted convert str values to lower case.
word = str.lower(input('Enter Word: '))

# Performing string comparisons through putting words in alphabetical order.
if word == 'banana':
    print("All right, bananas.")
elif word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')
