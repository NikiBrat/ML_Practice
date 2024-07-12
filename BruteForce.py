import string 

def Decipher(code, offset):
    new_code = ""
    for i in code:
        #print("I am looking at: ", i)
        if i == " " or i == "!" or i == "?" or i == ".":
            new_code += i
        elif i in list(string.ascii_lowercase):
            index = list(string.ascii_lowercase).index(i)
            index = index + offset
            if index >= 26:
                index = index - 26
            print("Index is:",index , " and offset is: ", offset , " and item we found with index is: ", list(string.ascii_lowercase)[index])
            new_code += list(string.ascii_lowercase)[index]
            print("New code is: ", new_code)
        else:
            new_code += i
    print(new_code)

string.ascii_lowercase
list(string.ascii_lowercase)

code = "vhfinmxkl"
new_code = ""
offset = 0
decryptIndex = 0 
for i in range(0,26): # Once the count reaches -26 stop, hammer time
    Decipher(code, offset)
    offset = offset + 1

            