l =['kaduu', 'mote']
with open("donkey.txt") as f:
    content = f.read()
*
for word in l:
    content = content .replace(word, "####")
    with open("donkey.txt", "w") as f:
        f.write(content)