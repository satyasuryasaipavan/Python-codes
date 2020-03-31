n = input("enter the string:")
for i in n:
    print(chr(ord(i) + 1),end ="")#chr() is used to convert ascii values to character
    