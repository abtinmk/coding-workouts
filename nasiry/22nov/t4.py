myList = list(map(int, input().split()))
myList.sort()
x, y, z = myList
XXX = (x,y+1,z+2)
a, b, c = XXX
b =- 1
c =- 2

if (a+b > c):
    print(x+y+z)
else:
    print("invalid")