string = "PyThOn"
print("String :",string)
print("Number of characters:",len(string))
for i in range(1,len(string)+1):
    print(string[:i])
upper=0
lower=0
vowel=0
vowel1=0
for i in string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        print("invalid")

    if i.lower() in "aeiou" or "AEIOU":
        vowel+= 1
        print("Vowel:", i)
    
print("Upper case:",upper)
print("Lower case:",lower)
print("Number of vowels:", vowel)