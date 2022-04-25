secret_number = 10
guess_limit = 3
guess_count = 0
temp = 0

while guess_count < guess_limit:
    guess = int(input("Enter the number : "))
    temp += guess
    guess_count += 1

    if temp == secret_number:
        print("You Won !!!")
        break
else:
    print("Sorry, you failed :(")