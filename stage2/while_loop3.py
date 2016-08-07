import random

random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

print random_list

count_list = [0] * 11
index = 0

while index <len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index += 1

print count_list
