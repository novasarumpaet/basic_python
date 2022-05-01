def plus(num1, num2):
    p = num1+num2
    return p

def minus(num1, num2):
    m = num1 - num2
    return m

def times(num1, num2):
    t = num1 * num2
    return t

def dividedby(num1, num2):
    d = num1 / num2
    return d

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

result1 = plus(num1,num2)
result2 = minus(num1,num2)
result3 = times(num1,num2)
result4 = dividedby(num1,num2)

print(f"The result of {num1} plus {num2} is {result1}")
print(f"The result of {num1} minus {num2} is {result2}")
print(f"The result of {num1} times {num2} is {result3}")
print(f"The result of {num1} divided by {num2} is {result4}")