bil1 = int(input("Enter number 1 : "))
bil2 = int(input("Enter number 2 : "))

print("Before swap")
print(f"Number 1 is {bil1} and Number 2 is {bil2}")
print("\n")

temp = bil1
bil1 = bil2
bil2 = temp

print("After swap")
print(f"Number 1 is {bil1} and Number 2 is {bil2}")