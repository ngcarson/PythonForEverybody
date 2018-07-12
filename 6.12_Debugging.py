# in response lesson 5.5 to error occuring when blank input in entered, we have modified the codes in lines 4 (option 1) and 5 (option 2).
while True:
    line = input('> ')
    if line.startswith('#'):
    #if len(line) > 0 and line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
