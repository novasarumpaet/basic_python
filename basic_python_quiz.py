print("!!! Welcome to Basic Python Quiz !!!")
print("1. Playing The Quiz")
print("2. Quit")

ch = int(input("What is your choice ? "))

if ch==1 :
  p = input("Do you want to play ? ")
  if p.lower() == "yes":
    score = 0

    q1=input('What is the correct file extension for Python files ?')
    if q1.lower() == ".py":
      print("You're Correct!!!")
      score += 1
    else:
      print("Incorrect!")
    
    q2=input('Insert COMMENTS in Python ?')
    if q2.lower() == '#this is the comments':
      print("You're Correct!!!")
      score += 1
    else:
      print("Incorrect!")
    
    q3=input('How do you create a variable with the numeric value 20 ?')
    if q3.lower() == 'x = 20':
      print("You're Correct!!!")
      score += 1
    else:
      print("Incorrect!")

    print("CONGRATULATIONS !!! You got " + str(score) + " questions correct!")
    print("You got " + str((score / 3) * 100) + "%")

  else:
    print("Thanks for visit my Quiz, Have a nice day :) ")
else :
  print("Thanks for visit my Quiz, Have a nice day :) ")

