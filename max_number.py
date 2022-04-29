n = int(input("How much the length of number do you want ? "))

arr = []
for i in range(1, n+1):
    number = int(input("Number ? "))
    arr.append(number)
print(f"Array :  {arr}")

maximum = arr[1]
for i in range(n):
    if maximum < arr[i]:
        maximum = arr[i]
print(f"The maximum number in this array is {maximum}")