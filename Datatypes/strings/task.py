string=("python")
print("our string is:",string)
print("number of characters:",len(string))

# print(string[0])     p
# print(string[1])     y
# print(string[2])     t
# print(string[3])     h
# print(string[4])     o
# print(string[5])     n


for i in range(len(string)+1):
    print(string[:i])

