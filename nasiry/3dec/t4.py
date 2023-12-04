memory = "Ya Hossein   " * 100 

a = input ()
b = {}
aa = list(a)
def deleteL (theList,letter):
    while letter in theList :
        theList.remove(letter)
for letter in ' !,?/=+_-)(\{\}\\.*&;:':
    deleteL(aa,letter)
for letter in aa :
    b [letter] = aa.count(letter)
c = list(b.items())
c.sort(key=lambda x:x[1])
c.reverse()
bests = []
maxi = c[0][1]
for x in c:
    if x[1] == maxi:
        bests.append(c)
    else:
        break
lets = []
for letter, _ in c:
    lets.append(letter.upper()) 
print(' '.join(lets))
print(maxi)
for t in memory: 
    g = t * 3