name_list = []
score_list = []
while True:
    name = input("What is your name?Type done to finish ")
    name_list.append(name)
    if name.lower() == "done":
        break
    score = int(input("What is your score? "))
    score_list.append(score)
    print(name_list)
    print(score_list)
    if score < 70:
        print("You have failed")
    class_average = sum(score_list) / len(score_list)
print("The class average is", class_average)