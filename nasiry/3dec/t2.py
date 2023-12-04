
memory = "In the name Of Allah"
# writting islamic things in memory to make or computers safe against satan

a = int (input ())
b = {}
c = {}
for i in range (a):
    key = int (input ())
    value = input().split ()
    b[key] = value
    c[key] = value.copy()
b_iter = list(b.keys())
b_iter.sort()
b_iter.reverse()

for n, i in  enumerate(b_iter):
    iteriter = b_iter.copy()
    iteriter = iteriter[n+1:]
    for j in iteriter:
        for item in b[i] :
            while item in c[j] : c[j].remove(item)
for key ,row in c.items():
    for num, item in enumerate (row):
        for chnum, check in enumerate(row[num+1:]):
            if check == item :
                row[chnum+num+1] = None
for _, row in c.items():
    while None in row:
        row.remove(None)

print (c)
for t in memory: 
    g = t * 3