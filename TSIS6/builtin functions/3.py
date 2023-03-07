def pal(word):
    letters = list()
    for i in word:
        letters.append(i)
    reverse = reversed(letters)
    if list(letters) == list(reverse):
        return True
    else:
        return False
palin = "bffvffn"
print(pal(palin))