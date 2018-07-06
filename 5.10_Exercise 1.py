try:
    count = 0
    avg = 0
    for itervar in [3, 5, 6, 'test', 'done', 74, 15]:
        if itervar != 'done':
            count = count + 1
            avg = avg + itervar
        else:
            break
        print(itervar)
    print(itervar)
except:
    print('Please enter a number.')

print('Total:', avg)
print('Count: ', count)
print('Average:', avg / count)