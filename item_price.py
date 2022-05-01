item = int(input("how many items do you want to buy?"))

if item>=150:
    price = item*9000
elif item>=100 and item<150:
    price = item*9500
elif item<100:
    price = item*10000

print(f"The total price of your item is {price} with {item} items")