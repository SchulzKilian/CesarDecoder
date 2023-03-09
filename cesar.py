import enchant
def changed(word,i):
    newword = ""
    for letter in word:
        pos = alph.find(letter)
        if pos + i <= 25:
            newword += alph[pos+i]
        else: 
            newword += alph[pos+i - 25]
    return newword
alph = "abcdefghijklmnopqrstuvwxyz"
x = input("Input the message you want to decode please")
d = enchant.Dict("en_US")
scores = {}
truei = -1
for i in range(0,26):
    newword = ""
    score = 0
    for word in x.split(" "):
        newword += " "+ changed(word,i)
        if d.check(changed(word,i)):
            score += 1
        if score <i/2 & i > 3:
            break
    scores[i]=(score,newword)
    truei = max(score,truei)

print(f"We believe your sentence might have been {scores[truei][1]} with the decoding factor {truei}.")







