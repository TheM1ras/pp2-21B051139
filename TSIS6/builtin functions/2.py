def uplow(words):
    numup = int(0)
    numlow = int(0)
    for a in words:
        if a.isupper():
            numup +=1
        elif a.islower():
            numlow+=1
        else:
            continue
    return numup, numlow
sentence = str(input())
print(uplow(sentence))