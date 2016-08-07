def average(list):
    ave = 0
    total = 0
    for num in list:
        total += num
    ave = total / len(list)
    return ave

def let_for(s,e):
    list = []
    for num in range(s,e):
        list.append(num)
    return list

print average(let_for(0,15))
