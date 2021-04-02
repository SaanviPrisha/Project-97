import random

randomNumber = random.randint(1, 9)

limit = 0

while(limit < 5):
    try:
        userAnswer = int(input("Guess A Number From 1 to 9 : "))
        if(userAnswer > 9 or userAnswer < 1):
            print("Pleases Give Correct Input")
    except:
        print("Pleases Give Correct Input")

    if(userAnswer == randomNumber):
        print("Congratulations!! Your Guess Is Correct")
        limit = 6
    elif (userAnswer > randomNumber):
        print("Your Guess is Bigger than My number")
    elif (userAnswer < randomNumber):
        print("Your Guess is Smaller than My number")

    limit = limit + 1

if(limit == 5):
    print("Your Chances Are Completed")
    print(f'Your number was {randomNumber} ')