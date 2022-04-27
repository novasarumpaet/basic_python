name = input("Student Name : ")
s_class = input("Student Class : ")
score = int(input("Score : "))

if score>=85 and score<=100:
    print(f"{name} student in class {s_class} get score {score} with A index")
elif score>=75 and score<=84:
    print(f"{name} student in class {s_class} get score {score} with B index")
elif score>=65 and score<=74:
    print(f"{name} student in class {s_class} get score {score} with C index")
elif score>=55 and score<=64:
    print(f"{name} student in class {s_class} get score {score} with D index")
elif score>=0 and score<=54:
    print(f"{name} student in class {s_class} get score {score} with E index")