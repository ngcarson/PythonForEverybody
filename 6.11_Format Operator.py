# https://docs.python.org/3.5/library/stdtypes.html#printf-style-string-formatting
camels = 42
print('%d' % camels)
print('I have spotted %d camels.' % camels)

# “%d” to format an integer, “%g” to format a floatingpoint number (don’t ask why), and “%s” to format a string
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
