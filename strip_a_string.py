def remove_split(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()

this ="Hello how are you doing???"
n = remove_split(this,"Hello")
print(n)
print(this)
print(this.strip)

