# You need to create a calculator function, but the calculator function has to take the value
# from the parameterized constructor. So while creating the object, you will pass the parameters
# and that will basically return the sum of the two numbers, multiplication of two numbers.

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        return self.num1+self.num2

    def multiplication(self):
        return self.num1*self.num2

    def division(self):
        return self.num1/self.num2

    def substraction(self):
        return self.num1-self.num2

cal=Calculator(30,15)
print(cal.sum())
print(cal.multiplication())
print(cal.division())
print(cal.substraction())


