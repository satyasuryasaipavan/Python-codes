#method1
n = input("enter the string:")
n = list(set(n))
print(''.join(n))
#note - this method was easy but the drawback is order of the letters in the string will be changed
#method2
n = input("enter the string:")
l = list(n)
for i in l:
    count = l.count(i)
    while (count != 1):
        l.remove(i)
        count  = count - 1
print(''.join(l))