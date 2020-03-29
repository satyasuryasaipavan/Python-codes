a = int(input("enter a value:"))
b = int(input("enter a value:"))
#method1 - using ++ operator

while (b != 0):
    a += 1
    b -= 1
print("the sum is :",a)

#method2 - using eval

a = int(input("enter a value:"))
b = int(input("enter a value:"))
print(eval('a+b'))

#method3 - using extend
a = int(input("enter a value:"))
b = int(input("enter a value:"))
l = []
l.extend((a,b))
print("the sum is:",sum(l))

