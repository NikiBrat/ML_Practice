import string 
string.ascii_lowercase
list(string.ascii_lowercase)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
new_code = ""
keyword = "friends"
decryptIndex = 0
for i in code:
    #print("I am looking at: ", i)
    if i == " " or i == "!" or i == "?" or i == ".":
        new_code += i
    elif i in list(string.ascii_lowercase):    
        index = list(string.ascii_lowercase).index(i)
        #print("Index is: ", index)
        offset = list(string.ascii_lowercase).index(list(keyword)[decryptIndex])
        #print("Offset is: ", offset)
        index = index + offset
        if index >= 26:
            index = index - 26
        #print("I am looking at letter with index: ", index, " and letter is: ", list(keyword)[index])
        new_code += list(string.ascii_lowercase)[index]
        decryptIndex = decryptIndex + 1
        if decryptIndex == len(keyword):
            decryptIndex = 0
print(new_code)