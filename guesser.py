import random


print("Hello! I am going to try to guess your age!")
name = input("What is your name? ")

guessed = False
while guessed == False:
    guess = random.randint(15,30)
    user_response = input("Are you "+str(guess)+"years old?")
    if user_response == "y" or user_response == "Y":
        print(f"Haha! {name} is " + str(guess) + " years old! I guessed it")
        guessed = True

    else:
        print("Rats.")