import random


print("Hello! I am going to try to guess your age!")
name = input("What is your name? ")

guesses = []
guessed = False
while guessed == False:
    guess = random.randint(15,30)
    if guess in guesses:
        continue

    user_response = input("Are you "+str(guess)+" years old? ")
    if user_response == "y" or user_response == "Y" or user_response == "yes" or user_response == "Yes":
        print(f"Haha! {name} is " + str(guess) + " years old! I guessed it")
        guessed = True

    else:
        print("Rats.")
        guesses.append(guess)