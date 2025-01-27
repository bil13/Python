#retrieves the user's name.
name = input("What is your name? ")
#asks for the subject.
subject = input("What subject do you need to study? ")
#asks for the study hours.
study_hours = int(input("How many hours can you dedicate? "))
#divides the study hours into two.
sessions = study_hours / 2
#creates a studying schedule.
print("Hi", name + "!", "You plan to study", subject, "for", study_hours, "hours. Divide this into 2 sessions of", sessions, "hours each with a 15 minute break in between. Stay focused" + ".")