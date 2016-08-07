def find_element(lists,value):
    i = 0
    for item in lists:
        if item == value:
            return i
        i=i+1
    return -1

print find_element([1,2,3],2)
print find_element([1,2,3],4)

p = [0,1,2,3]
print 3 in p
print p.index(5)

def find_element(p,v):
    if v in p:
        return p.index(v)
    else:
        return -1

print find_element([1,2,3],1)
print find_element([1,2,3],4)
