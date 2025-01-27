#this codes retrieves the user's name.
name = input("What is your name? ")
#this asks the user how many steps were taken today.
steps = int(input("How many steps have you taken today? "))
#this asks for the daily step goal.
goal = int(input('What is your daily step goal? '))
#this is the difference between the user's steps and the goal.
difference = goal - steps
#motivation
print("Hi", name + "!", "You have walked", steps, "steps today. Keep walking just", difference, "steps more to hit your goal.")