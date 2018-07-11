#A method call is called an invocation; in this case, we would say that we are invoking upper on the word.

word = 'banana'
new_word = word.upper()
print(new_word)

# For example, there is a string method named find that searches for the position of one string within another:
word = 'banana'
index1 = word.find('a')
print(index1)

# It can take as a second argument the index where it should start:
index2 = word.find('na', 3)
print(index2)

# One common task is to remove white space (spaces, tabs, or newlines) from the beginning and end of a string using the strip method:
line = '  Here we go  '
line1 = line.strip()
print(line1)

# Some methods such as startswith return boolean values
line = 'Have a nice day'
line2 = line.startswith('Have')
line3 = line.startswith('h')
print(line2)
print(line3)

# You will note that startswith requires case to match, so sometimes we take a line and map it all to lowercase before we do any checking using the lower method.
phrase = 'Have a nice day'
line4 = phrase.lower().startswith('h')
print(line4)

# https://docs.python.org/3.5/library/stdtypes.html#string-methods
word1 = 'banana banana banana'
word2 = word1.count('banana')
print(word2)
