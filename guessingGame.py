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
        print("Congratulations!! Your guess is correct")
        limit = 6
    elif (userAnswer > randomNumber):
        print("Your guess is bigger than the number")
    elif (userAnswer < randomNumber):
        print("Your guess is smaller than the number")

    limit = limit + 1

if(limit == 5):
    print("Your chances are completed")
    print(f'Your number was {randomNumber} ')
