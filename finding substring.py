n = input("enter the string:")
s = input("enter the substring:")
n = list(n)
s = list(s)
c = 0
for i in range(len(n)):
    count = 0
    if (n[i] == s[count]):
        for j in range(len(s)):
            if ( i + j < len(n) and n[i + j] == s[j]):
                count = count + 1
        if count == len(s):
            c = c + 1
print("the count is :",c)