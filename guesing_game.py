import random as rd # random module import statement
k = rd.randint(1, 10) # randomly generated number
n = 10 # number of chances

# some messages
print("Welcome to the guessing game in python")
print("Please enter a number between 1 and 10 (both included) -> ")
print("You have only 10 chances...")

# check loop
while(True):

    if n == 0 or n < 0:
        print("Game over")
        break

    x = int(input("Enter a number here : "))

    if x == k:
        print("You guessed right")
        break
    if x > k :
        print("You guessed too high!")
        --n
    if x < k :
        print("You guessed too low!")
        --n