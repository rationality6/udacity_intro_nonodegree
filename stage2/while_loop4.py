import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

number = 0
print "number | occurrence"
while number < len(count_list) :
    if number < 10:
        print " "*4, number ,"|" ,count_list[number]
    else:
        print " "*3, number ,"|" ,count_list[number]
    number += 1

number = 0
print "number | occurrence"
while number < len(count_list) :
    if number < 10:
        print " "*4, number ,"|" ,'*' * count_list[number]
    else:
        print " "*3, number ,"|" ,'*' * count_list[number]
    number += 1
