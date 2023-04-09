print("Welcome to the quiz game!")

play = input("Do you want to play the game? \nYes/No:")

if play.lower() != 'yes':
    quit()

name = input("Enter your name: ").title()
print("Let's begin the game :)")

score = 0

#Question 1
print("Ques 1.) What is the capital city of Australia?")
print("a)Sydney\tb)Melbourne")
print("c)Perth\t\td)Canberra")
answer = input("Answer: ")
if answer=='d':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 2
print("Ques 2.) Which planet is known as Red Planet in our solar system?")
print("a)Mercury\tb)Venus")
print("c)Mars\t\td)Uranus")
answer = input("Answer: ")
if answer=='c':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 3
print("Ques 3.) What is the world's largest ocean?")
print("a)Indian Ocean\t\tb)Pacific Ocean")
print("c)Atlantic Ocean\td)Arctic Ocean")
answer = input("Answer: ")
if answer=='b':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 4
print("Ques 4.) Which famous scientist developed the theory of relativity")
print("a)Albert Einstein\tb)Issac Newton")
print("c)Nikola Tesla\t\td)Rutherford")
answer = input("Answer: ")
if answer=='a':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 5
print("Ques 5.) What is the smallest country in world by land?")
print("a)Bangladesh\tb)Nepal")
print("c)San Marino\td)Vatican City")
answer = input("Answer: ")
if answer=='d':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 6
print("Ques 6.) Who is the founder of Microsoft?")
print("a)Elon Musk\t\tb)Bill Gates")
print("c)Stewe Jobs\td)Jeff Bezos")
answer = input("Answer: ")
if answer=='b':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 7
print("Ques 7.) Which animal is known as the \"Ship of the Desesrt\"?")
print("a)Tiger\t\tb)Lion")
print("c)Camel\t\td)Dog")
answer = input("Answer: ")
if answer=='c':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 8
print("Ques 8.) What is the highest mountain peak in the world?")
print("a)Kanchenjunga\t\tb)Mount McKinley")
print("c)Mount Everest\t\td)Mount Kailash")
answer = input("Answer: ")
if answer=='c':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 9
print("Ques 9.) In what year did India declare its independence from Great Britain?")
print("a)1947\t\tb)1946")
print("c)1948\t\td)1888")
answer = input("Answer: ")
if answer=='a':
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 10
print("Ques 10.)What is the largest organ in human body?")
print("a)Liver\t\tb)Heart")
print("c)Lungs\t\td)Skin")
answer = input("Answer: ")
if answer=='d':
    print("Correct")
    score += 1
else:
    print("Incorrect")


print("Your score is: " + str(score))
print("You got " + str((score/10)*100) + "%")

if score == 10 or score == 9:
    print("Excellent " + '"' + name + '"')
elif score == 8 or score == 7:
    print("Very Good " + '"' + name + '"')
elif score == 6 or score == 5:
    print("Nice " + '"' + name + '"')
elif score == 4 or score == 3:
    print("Try better " + '"' + name + '"')
elif score == 2 or score == 1:
    print("You need to learn " +  '"' + name + '"')
else:
    print("Are you serious " +  '"' + name + '"')