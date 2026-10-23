#Write a program to count the number of vowels, consonants, digits, spaces,and special characters in a given string
string="Python Django Full@Stack_b1"
print("String is:",string)
print("Number of digits:",len(string))
vowels=0
consonants=0
digits=0
spaces=0
special=0
for i in string:
    if i.lower() in 'aeiou':
        vowels+=1
    elif i.isnumeric():
        digits+=1
    elif i.isspace():
        spaces+=1
    elif i.isalpha():
        consonants+=1
    else:
        special+=1

print("Vowels",vowels)
print("consonants",consonants)
print("Digits",digits)
print("Spaces",spaces)
print("Special",special)