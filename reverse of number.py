n = int(input("enter given number:"))

#by using while loop
rev  = 0
while (n!=0):
    rev = rev * 10 + n % 10
    n =  n // 10
print(rev)

#using slicing

n = input("enter given number:")
print(n[::-1])

