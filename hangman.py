
hangmanword = "dinosaur"
letterlist = list(hangmanword)
triedlist =[]
lives = 0
from hangman2 import  *
#print(letterlist)  # see what letters are in our word
displaylist = [] # display underscored
for i in letterlist:
    displaylist.append("_")


def letterguess():# guess a letter
    global letterlist
    global lives
    guess = input("Guess a letter : ")
    counter = 0
    y =0
    for i in letterlist:# guess right letter
        if guess == i:
            displaylist.pop(counter)
            displaylist.insert(counter,guess)
            y = 1
        counter = counter + 1
    if y == 0:
        triedlist.append(guess)# pick wrong letter
        lives = lives +1
        print("The letter is not part of word")


x = True
while x == True:
    letterguess()
    print(displaylist)
    print(triedlist)
    print(HANGMANPICS[lives])
    if lives == 6:
        print("you lose") #lose screen
        break

    elif "_" not in displaylist:
        print("you win") #win screen
        break


