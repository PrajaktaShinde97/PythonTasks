# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

number = int(input("Enter a number for factorial : "))
factorial = 1
if number < 0:
    print("Enter a valid number")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number+1):
        factorial=factorial*i
print("factorial is - ",factorial)






