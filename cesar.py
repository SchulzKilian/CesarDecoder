import nltk
nltk.download("words")
from nltk.corpus import words
word_list = set(words.words())
def changed(word,i):
    newword = ""
    for letter in word:
        pos = alph.find(letter.lower())
        if pos + i <= 25:
            newword += alph[pos+i]
        else: 
            newword += alph[pos+i - 25]

    return newword
alph = "abcdefghijklmnopqrstuvwxyz"
x = input("Input the message you want to decode please")

scores = {}
truei = -1
highscore = -1
for i in range(0,26):
    newword = ""
    score = 0
    for k,word in enumerate(x.split(" ")):
        newword += " "+ changed(word,i)
        if changed(word,i) in word_list:
            score += 1
        if float(score) <k/2 and float(k) > 3.0:
            break
    scores[i]=(score,newword)

    if score > highscore:
        highscore=score

        truei = i

print(f"We believe your sentence might have been {scores[truei][1]} with the decoding factor {truei}.")







