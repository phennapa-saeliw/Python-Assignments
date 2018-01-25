#Libraries and Functions always come in handy to developers by allowing reusability of existing code. There are certain well known inherent libraries that you have access to after installing python. By using these libraries and functions in them, write a program to guess a randomly generated number between 1 and 10. 
#For Example: 

#Guess the number: 4
#Wrong, try again! 

#Guess the number: 8
#Correct! 

#Hint: Figure out which library the “randint” function belongs to. 


import random

randomNumber = random.randint(1,10)
#print("randomNumber: "+str(randomNumber))
number = int(input("Guess the number: "))
if randomNumber == number:
    print("Correct!")
else:
    print("Wrong, try again!")