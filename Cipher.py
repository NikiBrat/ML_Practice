import string 
string.ascii_lowercase
list(string.ascii_lowercase)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = "thank you for your message! i am glad I was able to decipher it! see you!"
new_code = ""
for i in code:
    #print("I am looking at: ", i)
    if i == " " or i == "!" or i == "?" or i == ".":
        new_code += i
    elif i in list(string.ascii_lowercase):
        index = list(string.ascii_lowercase).index(i)
        #print("Index is: ", index)
        index = index - 10
        if index < 0:
            index = index + 26
        new_code += list(string.ascii_lowercase)[index]
    else:
        new_code += i
print(new_code)