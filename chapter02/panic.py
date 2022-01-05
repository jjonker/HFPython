phrase = "Don't panic!"
target = "on tap"

plist = list(phrase)
print(phrase)
print(plist)

found = []
for letter in plist:
    if letter in target:  
        if letter not in found:
            found.append(letter)

plist = found

space = plist.pop(3)
plist.insert(2, space)
a_char = plist.pop()
plist.insert(4, a_char)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
