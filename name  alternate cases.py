n = input("enter name:")
n = list(n)
n = [n[x].upper() if x%2 != 0 else n[x] for x in range(len(n))]#using list comprehensions
print(''.join(n))

 #same code without list comprehensions
n = input("enter name:")
n = list(n)
for x in range(len(n)):
     if (x % 2 != 0):
         print(n[x].upper(),end = "")
     else :
         print(n[x],end="")