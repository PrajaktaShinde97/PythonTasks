# Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

side1 = int(input("Enter side1 : "))
side2 = int(input("Enter side2 : "))
side3 = int(input("Enter side3 : "))

def triangle(s1,s2,s3):
    if s1 == s2 == s3:
        print("Triangle is Equilateral Triangle")
    if s1== s2 != s3:
        print("Triangle is Isosceles Triangle")
    if s1 != s2 != s3:
        print("Triangle is Scalene Triangle")

triangle(side1,side2,side3)
