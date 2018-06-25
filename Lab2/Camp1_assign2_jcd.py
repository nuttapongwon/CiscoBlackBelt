import random

ran = random.randint(1,10)

while True:
    guessNo = input("Please Guess the number : ")
    if int(guessNo) == int(ran):
        print("Correct!")
        break
    elif (int(guessNo) != int(ran)):
        print("Wrong, try again! ")