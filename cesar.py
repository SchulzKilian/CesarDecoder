import nltk
nltk.download("words")
from nltk.corpus import words
word_list = set(words.words())
def removespecials(word):
    newword = ""
    for letter in word:
        if letter.lower() in alph:
            newword+=letter
    return newword

def changed(word,i):
    newword = ""
    for letter in word:
        pos = alph.find(letter.lower())
        if pos + i <= 25:
            newword += alph[pos+i]
        else: 
            newword += alph[pos+i - 26]

    return newword
alph = "abcdefghijklmnopqrstuvwxyz"
x = input("Input the message you want to decode please\n\n")

scores = {}
truei = []
highscore = -1
for i in range(0,26):
    newword = ""
    score = 0
    for k,word in enumerate(x.split(" ")):
        newword += " "+ changed(removespecials(word),i)
        if changed(removespecials(word),i) in word_list:
            score += 1
    
        if float(score) <k/3 and float(k) > 3.0:
            break
    scores[i]=(score,newword)

    if score > highscore:
        highscore=score

        truei = [i]
    elif score == highscore:
        truei.append(i)

print("Possible encryptions might be: \n\n") 
for tru in truei: 
    print(f"\nWe believe your sentence might have been: \n\n {scores[tru][1]} with the decoding factor of {26-tru}\n\n")








