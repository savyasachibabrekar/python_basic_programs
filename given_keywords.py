
text = input("Enter the text")
spam=False

if("make a lot of money"):
    spam=True
elif("buy now" in text):
    spam=Ture
elif("click this" in text):
    spam=Ture
elif ("subscribe" in text):
    spam=Ture
else:
    spam=False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
