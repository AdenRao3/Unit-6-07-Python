# Created by: Aden Rao
# Created on: April 12, 2019
# This program lets the user guess my age and it gives them hints as to if I am older or younger each time they guess 

# Age to guess variable and the users guess through input
myAge = 15
Guess = int(input("Try to guess my age: "))

# While loop to determine if they guessed my age
while myAge != Guess:
	if Guess > myAge:
		print ("I'm younger than this. Try again!")
		Guess = int(input("Try to guess my age: "))

	if Guess < myAge: 
		print ("I'm older than this. Try again!")
		Guess = int(input("Try to guess my age: "))
		
	if Guess == myAge:
		print ("You guessed my age!")
		break