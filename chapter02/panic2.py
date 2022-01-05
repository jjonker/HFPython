phrase = "Don't panic!"

plist = list(phrase)
print(phrase)
print(plist)

# remove "nic!"
for i in range(4):
    plist.pop()
# remove "D"
plist.pop(0)
# remove "'"
plist.remove("'")
# swap p and a
plist.extend([plist.pop(), plist.pop()])
# remove the space and insert it in the right place
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
