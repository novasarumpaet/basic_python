print("=====================")
print("Welcome to my coffee shop")
print("=====================")
print("\n")

name = input("Enter your name : ")
print("This is the list of my coffee shop")
print("1. Americano")
print("2. Expresso")
print("3. Cappucchino")
print("4. Cafe latte")
print("5. Machhiatto")

n = int(input("How much item do you want to buy ? "))

total = 0
for i in range(1, n+1):
    buy = input("What do you want to buy ? ")

    if buy.lower() == "americano":
        total += 55000
    elif buy.lower() == "expresso":
        total += 26000
    elif buy.lower() == "cappucchino":
        total += 56000
    elif buy.lower() == "cafe latte":
        total += 39000
    elif buy.lower() == "machhiatto":
        total += 45000
    else:
        print("Your choice is not mention on own list")
        break

print(f"total without discount {total}")

if total >= 150000:
    disc = total * (0.1)
    result = total - disc
else:
    result = total


print(f""""
Thanks {name} for your order
Your total price is {result}
Have a nice day :)
""")

