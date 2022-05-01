print("1. Plus")
print("2. Minus")
print("3. Times")
print("4. Divided by")
print("\n")

pil = input("What is your choice : ")
bil1 = int(input("Number 1 : "))
bil2 = int(input("Number 2 : "))

if pil.lower()=="plus":
    result = bil1+bil2
elif pil.lower()=="minus":
    result = bil1-bil2
elif pil.lower()=="times":
    result = bil1*bil2
elif pil.lower()=="divided by":
    result = bil1/bil2

print(f"The result of {bil1} {pil} {bil2} is {result}")