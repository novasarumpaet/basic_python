print("==============================")
print("the average of student scores")
print("==============================")

mhs_count = int(input("Enter the number of student ? "))
total = 0

for i in range(1, mhs_count+1):
    name = input("Name : ")
    nim = input("NIM : ")
    score = int(input("Score : "))
    print("======================")
    print("\n")

    total += score

print(f"The average of student scores : {total/mhs_count}")
