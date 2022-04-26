print("=================")
print("Employee Fee")
print("=================")

name = input("Enter the Employee Name : ")
print("1. Group I")
print("2. Group II")
print("3. Group III")
group = int(input("Enter the group : "))
time = int(input("Enter the overtime hours : "))

if group == 1:
    fee = 250000
elif group == 2:
    fee = 500000
elif group == 3:
    fee = 750000

fix_fee = 0.25*fee
overtime_bonus = time*fix_fee
total_salary = fee + fix_fee + overtime_bonus

print("\n")
print("-----Total Salary-----")
print(f"Employee Name : {name}")
print(f"Group : {group}")
print(f"Overtime hours {time}")
print(f"Salary : Rp. {total_salary}")

