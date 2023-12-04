
a = input ().split ()
b = []
count = 0
for i in a :
    b. append(float (i))
    count +=1
m = (sum (b)/count)
print ( round (m ,3))
L = []
A = []
H = []
for t in b :
    if 9<= t<=10 :
        H.append(t)
    elif 7<= t <=8 :
        A.append (t)
    elif 1<=t <=6 :
        L.append(t)
Level = {"High" : len (H), "Average" : len (A) , "Low": len(L)}
print (Level) 
if len(A) == 0 and len(L) ==0 :
    print("They did well")
