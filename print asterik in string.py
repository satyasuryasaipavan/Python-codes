n = input("enter the string:")
l = []
for i in n:
    l.append(i)
    if i.isnumeric():#string.isnumeric is used to check whether the string is number or not
        for i in range(int(i)):
            l.append('*')
print(''.join(l))