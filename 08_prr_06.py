def remove_and_strip(string, word):
    new_str = string.replace(word, "")
    return new_str.strip()
this = "          I am Chetana      "
f = remove_and_strip(this, "Chetana")
print(f)