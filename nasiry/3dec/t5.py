cache = {
    1:{0:1}
}

# 1 : {0:1}
# 2 : {-1:1, 1:1}
# 3 : {-1:1,0:2,1:1}
# 4 : {-2:1 -1: 1: 2:}
# 5 : {-2:1 -1: 0: 1: 2:}
def get_number_from_row(row, num):
    odd = len(row)%2==1
    if num in row:
        return row[num]
    if num==0 and not odd:
        return get_number_from_row(
            row,
            1
        )
    return 0
def get_row(num):
    if num in cache :
        return cache[num]
    odd = num%2==1
    new_row = {}
    maximmum = round((num)/2-0.1)
    last_row = get_row(num-1)
    def iter():
        if odd:
            return range(-maximmum, maximmum+1)
        else :
            ret = list(range(-maximmum, maximmum+1))
            ret.remove(0)
            return ret

    for i in iter():
        a = get_number_from_row(
            last_row,
            i
        )
        if odd :
            b = get_number_from_row(
                last_row,
                i-1 if i < 0 else i+1
            )
        else:
            b = get_number_from_row(
                last_row,
                i-1 if i >= 0 else i+1
            )
        new_row[i]= a+b
    cache[num] = new_row
    return new_row
def get_sum_of_row(row):
    return sum(map(lambda x:x[1],row.items()))
inp = int(input())
list_of_numbers=[]
for i in range(1,inp+1):
    row = get_row()
    sum_of_row = get_sum_of_row(row)
    list_of_numbers.append(sum_of_row)
for i in list_of_numbers:
    print(i)