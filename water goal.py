name = input("What is your name? ")
age = input("How old are you? ")
daily_goal = int(input("What is your daily goal? "))
current = int(input("How many cups of water have you drank? "))
difference = daily_goal - current
print("Hi", name + ",", "You drank", current, "cups of water, You need to drink", difference, "more cups to hit your goal.")