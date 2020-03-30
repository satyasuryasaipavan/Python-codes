n = int(input("enter the range:"))
n1 = (n * 2) - 1
mid = n1 // 2
c = 0
for i in range(n):
    for j in range(n1):
        if (j >= mid - c and j <= mid + c ):
            print('*',end = "")
        else :
            print(" ",end = "")
    print()
    c =  c + 1