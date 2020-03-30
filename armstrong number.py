#method1 - using list
n = input("enter given number:")
k = list(n)
k = [int(x) ** len(k) for x in k]
if (sum(k) == int(n)):
    print("it is a armstrong number")
else :
    print("not a armstrong number")

#method2
n = input("enter given number:")
k = int(n)
l = len(n)
sum = 0
while(k != 0):
    sum = sum + (k % 10) ** l
    k = k // 10
if sum == int(n):
    print("it is a armstrong number")
else:
    print("not a armstrong number")


