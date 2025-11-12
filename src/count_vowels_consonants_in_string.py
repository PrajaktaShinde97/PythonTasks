# count vowels and consonants in a string
string = "automation"
vowels = "aeiou"
vowels_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowels_count = vowels_count + 1
    else:
        consonant_count = consonant_count + 1

print("vowels are - ", vowels_count)
print("consonants are - ",consonant_count)


# if do not want to repeat the count of vowels and consonant
vowels_count = 0
consonant_count = 0
unique_set = set()

for char in string:
    if char in vowels:
        if char not in unique_set:
            vowels_count = vowels_count + 1
            unique_set.add(char)

print(vowels_count)










