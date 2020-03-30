for i in range(10):
    for j in range(5):
        if i == 0 or i == 5 or j == 0:
            print(" * ",end = "")
        elif(j == 4 and i <= 4):
            print(" * ", end="")
        else:
            print("   ",end = "")
    print()
