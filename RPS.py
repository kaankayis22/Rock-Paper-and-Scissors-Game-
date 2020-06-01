import random

UI = str(input("Welcome to Rock Paper Scissors! What will you play? Please enter 'rock' 'paper' or 'scissors'  : "))
rand1 = random.randint(0,2)

if UI == "Who made this?":
    print("Kaan Kayis did")
elif UI == "" or UI == " " or UI == "haha look at me, defing the rules. i am so funny arn't i! HAHAHAHHA":
    print("I SAID A PICK ONE!!!!")
x=0

if UI == "Rock" or UI == "rock":
    x=1
elif UI == "Scissors" or UI == "scissors":
    x=2
elif UI == "Paper" or "paper":
    x=3

if rand1 == 0:
    print("Bot chooses Rock!")
if rand1 == 1:
    print("Bot chooses Scissors!")
if rand1 == 2:
    print("Bot chooses Paper!")

if x == 1 and rand1 == 2:
    print("You LOSE!")
elif x == 2 and rand1 == 1:
    print("DRAW!")
elif x == 3 and rand1 == 0:
    print("You WIN!")
elif x ==  1 and rand1 == 1:
    print("You WIN!")
elif x == 2 and rand1 == 0:
    print("You LOSE")
elif x == 1 and rand1 == 0:
    print("DRAW!")
elif x == 2 and rand1 == 1:
    print("DRAW!")
elif x == 3 and rand1 == 2:
    print("DRAW!")
elif x == 2 and rand1 == 2:
    print("You WIN!")
elif x == 3 and rand1 == 1:
    print("You LOSE")
