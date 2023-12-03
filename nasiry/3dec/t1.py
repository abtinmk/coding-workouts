num = input ().split (", ")
a = []
for i in num :
    a.append(int (i))
sort = True
for t in range (len (a)-1):
    if a [t]>a [t+1]:
        sort = False
if sort == True :
    print("YES")
else :
    b= sorted(a)
    print (*b ,sep=", ")