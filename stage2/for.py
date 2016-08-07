example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country

def sum_list(list):
    total = 0
    for num in list:
        total += num
    return total

print sum_list([1,7,4])
print sum_list([])
print sum_list([9, 4, 10])
#>>> 23
print sum_list([44, 14, 76])
#>>> 134

def measure_udacity(p):
    count = 0
    for name in p:
        if name[0] == "U":
            count += 1
    return count

names=['Dave','Sebastion','Katy']

print measure_udacity(names)
print measure_udacity(['Umika','Umberto'])
