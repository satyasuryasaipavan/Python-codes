#method1 using regular expresions
import re
n = input("enter the string:")
n = re.findall("[a-zA-Z]",n)
print(''.join(n))

#method2 using ascii values
n = input("enter the string:")
n = list(n)
l = []
for i in n:
    if ((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):#here we are checking for alphabets only 
        l.append(i)
print(''.join(l))


