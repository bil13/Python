# asks for the user's name
name = input("What is your name? ")
# asks for the time
time_hour = int(input("What is the time? "))
# if condition for morning
if 12 > time_hour >= 5:
    print("Good morning", name + "!")
# condition for the afternoon (Fixed the condition)
elif 12 <= time_hour < 18:
    print("Good afternoon", name + "!")
# condition for the night
else:
    print("Good night", name + "!")

# asks for two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
# asks for the operation choice
operation = input("Choose +, -, /, * : ")
# performs the chosen operation
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)

# asks for the student's grade and attendance
grade = int(input("What was your grade in percentage? "))
attendance = int(input("What is your attendance in percentage? "))
# asks if the student has extra credit
extra_credit = input("Do you have extra credit? ")
# conditions for grading
if grade >= 90 and attendance >= 75:
    print("Grade A")
elif grade >= 90 and attendance < 75:
    print("Grade B")
elif 90 > grade >= 80 and extra_credit == "Yes":
    print("Grade A")
elif 90 > grade >= 80:
    print("Grade B")
elif grade <= 60 and attendance == 90:
    print("Grade D")
elif grade <= 60:
    print("You have failed")

# asks for the temperature and whether it is raining
temperature = int(input("What is the temperature in Celsius: "))
raining = input("Is it raining? ")

# checks weather conditions and gives advice
if temperature < 20 and (raining == "Yes" or raining == "yes"):
    print("It's cold and rainy, wear a warm jacket and grab an umbrella.")
elif temperature < 20 and (raining == "No" or raining == "no"):
    print("It's cold outside, wear a warm jacket.")
elif raining == "Yes" or raining == "yes":
    print("It's raining outside, grab an umbrella.")
else:
    print("The weather is good.")

# asks for the user's age
age = int(input("How old are you? "))
# determines the user's generation
if age >= 31:
    print("You are an oldhead.")
else:
    print("You are Gen Z, you are cooked.")

# asks if the user is a student
student = input("Are you a student? ")
# sets discount percentages
student_discount = 10
senior_discount = 15
# checks discount eligibility
if age >= 60 and (student == "Yes" or student == "yes"):
    print("You are eligible for a discount of", senior_discount, "%")
elif age >= 60 and (student == "No" or student == "no"):
    print("You are eligible for a discount of", senior_discount, "%")
elif age < 60 and (student == "Yes" or student == "yes"):
    print("You are eligible for a discount of", student_discount, "%")
else:
    print("Sorry, you are not eligible for a discount.")
