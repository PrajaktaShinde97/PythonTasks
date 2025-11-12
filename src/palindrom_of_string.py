# write a program of palindrome of string
string = input("Enter a string : ")
reverse_string = string[::-1]

if string == reverse_string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")










