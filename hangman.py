
hangmanword = "water"
letterlist = list(hangmanword)
triedlist =[]
lives = 0
from hangman2 import  *
#print(letterlist)  # see what letters are in our word
displaylist = [] # display underscored
for i in letterlist:
    displaylist.append("_")


def letterguess():
    global letterlist
    global lives
    guess = input("Guess a letter : ")
    counter = 0
    y =0
    for i in letterlist:
        if guess == i:
            displaylist.pop(counter)
            displaylist.insert(counter,guess)
            y = 1
        counter = counter + 1
    if y == 0:
        triedlist.append(guess)
        lives = lives +1
        print("The letter is not part of word")


x = True
while x == True:
    letterguess()
    print(displaylist)
    print(triedlist)
    print(HANGMANPICS[lives])
    if lives == 6:
        print("you lose")
        break

    elif "_" not in displaylist:
        print("you win")
        break


