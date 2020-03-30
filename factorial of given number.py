#method 1
n = int(input("enter given number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

#method 2
l = [x for x in range(1,n+1)]
prod = 1
for x in l:
    prod = prod * x
print(prod)