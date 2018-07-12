# https://docs.python.org/3.5/library/stdtypes.html#string-methods.

# find method which allows us to specify a position in the string where we want find to start looking

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

# we extract the characters from “one beyond the at-sign through up to but not including the space character”

host = data[atpos+1:sppos]
print(host)
