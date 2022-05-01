def isGenap(number):
    if number%2==0:
        return True
    else:
        return False

number = int(input("Enter the number : "))
result = isGenap(number)
print(f"{number} is the even number ? {result}")