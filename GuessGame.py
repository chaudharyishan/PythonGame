import random

print("\t\t\tWelcome to Guess- The Number Game")
print("\n")
print("\tRules: You have to guess the number which I am thinking out,\n\tI will give you a hint wheather the guess number is too HIGH,LOWER \n\tto thenumber which I have guessed")
print("\n\tScore Card: 1st Attempt= 50 Points")
print("\t\t    2nd Attempt= 40 Points")
print("\t\t    3rd Attempt= 30 Points")
print("\t\t    4th Attempt= 20 Points")
print("\t\t    5th Attempt= 10 Points")
print("\n\n")


guessNumber=random.randrange(10)+1;
attempt=0
score=50

userNumber=int(input("Enter the Number which Computer has Guessed between 1-10"))

while attempt<5:
  if userNumber==111:
      input("\nPress Enter to Exit")
      break
  else:
    if userNumber>guessNumber:
        if attempt<4:
            print("\tYour Number is HIGHER, Try Again with Lower Number")
            userNumber=int(input("\nEnter the Number which Computer has Guessed between 1-10"))
            attempt+=1
            score-=10
        else:
            print("\tYour Number is HIGHER")
            print("\n\t\tYou Loose the Game:(")
            print("\t\tYour Score is 0")
            print("\tHard Luck!, Nevermind better luck next time.")
            print("\n\t\t\tRemember!")
            print("You have lost Game not Life, so don't GIVE UP Try until successed")       
            attempt=0
            score=50
            print("When Tired, Simply Enter Number 111 to Exit the Game")
            userNumber=int(input("\nEnter the Number which Computer has Guessed between 1-10"))
    elif userNumber<guessNumber:
        if attempt<4:
            print("\tYour Number is LOWERER, Try Again with HIGH Number")
            userNumber=int(input("\nEnter the Number which Computer has Guessed between 1-10"))
            attempt+=1
            score-=10
        else:
            print("\tLower")
            print("\n\t\tYou Loose the Game:(")
            print("\t\tYour Score is 0")
            print("\tHard Luck!, Nevermind better luck next time.")
            print("\n\t\t\tRemember!")
            print("You have lost Game not Life, so don't GIVE UP Try until successed")
            attempt=0
            score=50
            print("When Tired, Simply Enter Number 111 to Exit the Game")
            userNumber=int(input("\nEnter the Number which Computer has Guessed between 1-10"))
    else:
        print("\n\t\tCongrats, You Guessed!")
        print("\t\tYour Score is ", score)
        print("\n\tThanks for Playing, Hope you have a Nice Day")
        break
input("\nPress Enter to Exit")      
        
