fhand = open('mbox-short.txt')

# Method 1 Search File
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)

# Method 2 Search File
for x in fhand:
    x = x.rstrip()
    # Skip 'uninteresting lines'
    if not x.startswith('From:'):
        continue
    # Process our 'interesting lines'
    print(x)

# Method 3 Search File
for y in fhand:
    y in y.rstrip()
    # -1 is if string is not found
    if y.find('@uct.ac.za') == -1: continue
    print(line)
