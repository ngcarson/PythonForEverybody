# Note, refer to lesson 6.12 for improvements in code to address error in blank inputs.

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
