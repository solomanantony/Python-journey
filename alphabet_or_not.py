a=input("enter character: " )
if len(a)==1 and a.isalpha():
    print("it's a single alphabet character")
elif a.isalpha():
    print("it's multiple alphabets")
else:
    print("it's not an valid alphabet character")