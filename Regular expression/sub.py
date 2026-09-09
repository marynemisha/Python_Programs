import re
sentence="Welcome to luminar"

x=re.sub("\s","_",sentence)
print(x)
#The sub() function replaces the matches with the text of
#your choice
#Here,replaces every white spaces with underscores.