# credit to @ZviNeug

import random

def word_chooser():
    wordChoices = ["falafel","abacus","missile","papyrus","chicken","decorate","trouble","lollipop","query","cabbage","noodle","balloon","television","calculus","walrus","whale"]
    return random.choice(wordChoices)

def main():
    print("HANG MAN")
    guesses = []
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h"\
               ,"j","k","l","z","x","c","v","b","n","m"]
    fails = 0

    word = word_chooser()
   
    while fails < 6:
        filled=0
        guess = None
        if fails==0:
            print("  ______ \n /        \n|\n|\n|\n~~~~~~~~~~")
        if fails==1:
            print("  ______ \n /      O\n|\n|\n|\n~~~~~~~~~~")
        if fails==2:
            print("  ______ \n /      O\n|       |\n|\n|\n~~~~~~~~~")
        if fails==3:
            print("  ______ \n /      O\n|      /|\n|\n|\n~~~~~~~~~~")
        if fails==4:
            print("  ______ \n /      O\n|      /|\\\n|\n|\n~~~~~~~~~~")
        if fails==5:
            print("  ______ \n /      O\n|      /|\\\n|      /\n|\n~~~~~~~~~~")
        for i in range(len(word)):
            if word[i] in guesses:
                print(word[i], end=" ")
                filled+=1
            else:
                print("_", end = " ")
        print("\n\n_____________________________")
        if filled==len(word):
            return "\nYOU WIN"
       
        print("Used letters:",end="")
        for i in range(len(guesses)):
            print(guesses[i],end="")
        print("\n")
        guess = input("Guess letter: ").strip().lower()
       
        while not guess in letters or guess in guesses:
            print("Invalid input")
            guess = input("Guess letter: ").strip().lower()
        print("_____________________________")
        if not guess in word:
            fails+=1

        guesses += [guess]
    print("  ______ \n /      O\n|      /|\\\n|      / \\\n|\n~~~~~~~~~")
    print("The word was:",word)
    return "OOF"
print(main())
