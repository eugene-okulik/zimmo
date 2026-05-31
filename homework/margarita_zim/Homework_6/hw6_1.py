text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
text = []

for word in words:
    if word.isalpha():
        word += "ing"
        text.append(word)
    else:
        word = word[:-1] + "ing" + word[-1]
        text.append(word)

text = " ".join(text)
print(text)
