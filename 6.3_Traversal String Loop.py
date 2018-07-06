#print traverse through a string loop (version 1)
fruit = 'banana'
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

print("\n")

#print traverse through a string loop (version 2)
for i in list(fruit):
    print(i)

print("\n")

#print reverse through a string loop (version 2)
for i in reversed(fruit):
    print(i)
