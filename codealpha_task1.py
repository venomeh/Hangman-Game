import random
import os
import time



# total wrong attempts for the user are 5
# user will enter words himself out of which he'll guess one
# which is randomly chosen by random.choice()

wrongAttempts = 5

while True:
    try:
        totalWords = int(input("How many words would you like to be in the list to choose one random one from? "))
        break
    except ValueError as E:
        print(E)
        print("kindly enter a valid NUMBER !!")
        time.sleep(1.5)

wordsList = []

print("Enter words that you would like to be in the list:")
for i in range(totalWords):
    word = input(f"Enter word {i + 1}: ")
    wordsList.append(word)

random.shuffle(wordsList)



# using a dictionary to store the unguessed word  and getting number of
# keys to get a to set loop condition

unguessedWord = random.choice(wordsList)
wordDict = {letter: False for letter in unguessedWord}
numberOfKeys = len(wordDict.keys())

while numberOfKeys > 0 and wrongAttempts > 0:
    print(wordsList)
    guess = input("Enter letter: ")

    # if a guessed word has already been guessed then it reduces the
    # wrong attempts count , otherwise it count it in as the letters
    # of the unguessed word

    if guess in wordDict:
        if wordDict[guess]:
            wrongAttempts -= 1
            print(f"Already guessed: Attempts remaining {wrongAttempts}")
            continue
        else:
            numberOfKeys -= 1
            print(f"You guessed it right: {guess}")
            wordDict[guess] = True

        print("Current state of the word:", ''.join([letter if wordDict[letter] else '_' for letter in unguessedWord]))

        if numberOfKeys == 0:
            os.system('cls' if os.name == 'nt' else 'clear') # to make clear screen work on all platforms
            print("Congratulations! You guessed the word.")
            break
    else:
        wrongAttempts -= 1
        print(f"Wrong guess: Attempts remaining {wrongAttempts}")
    
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

if wrongAttempts == 0:
    print(f"Sorry, you ran out of attempts. The correct word was: {unguessedWord}")
