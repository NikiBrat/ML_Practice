import string 
string.ascii_lowercase
list(string.ascii_lowercase)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
new_code = ""
offset = 7
for i in code:
    #print("I am looking at: ", i)
    if i == " " or i == "!" or i == "?" or i == ".":
        new_code += i
    elif i in list(string.ascii_lowercase):
        index = list(string.ascii_lowercase).index(i)
        index = index + offset
        if index >= 26:
            index = index - 26
        new_code += list(string.ascii_lowercase)[index]
    else:
        new_code += i
print(new_code)

            