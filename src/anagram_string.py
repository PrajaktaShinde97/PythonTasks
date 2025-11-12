# check if strings are namagram
string1 = input("Enter a string - ")
string2 = input("Enter a string - ")

if len(string1) != len(string2):
    print(f"{string1} and {string2} are not anagram")

sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

if sorted_string1 == sorted_string2:
    print(f"{string1} and {string2} are anagram")






