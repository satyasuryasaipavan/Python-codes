l = int(input("enter the length:"))
b = int(input("enter the breadth:"))
for i in range(b):
    for j in range(l):
        if (i == 0 or i == b - 1):
            print(' * ', end="")
        elif (j == 0 or j == l - 1):
            print(' * ', end="")
        else:
            print("   ", end="")
    print()