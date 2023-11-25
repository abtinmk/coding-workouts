import math

a, b, c = [float(x) for x in input().split()]
delt = ((b**2)-(4*a*c))

if delt<0:
    print("No roots")
elif delt==0:
    print(-b/2*a)
elif delt>0:
    xa = round(
        (-b+math.sqrt(delt))/(2*a), 
        1
        )
    xb = round(
        (-b-math.sqrt(delt))/(2*a), 
        1
        )
    if xb > xa :
        y, z = xb, xa
    else:
        z, y = xb, xa
    print(y, z)
