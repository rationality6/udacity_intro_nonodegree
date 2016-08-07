import random

status = 1
played_count = 0
winning_count = 0


def bomb():
    global status
    global played_count
    global winning_count
    is_explode = random.randrange(0, 2)
    if is_explode == 1:
        status = 0
        played_count += 1
        print "Exploded! You are dead."
    else:
        played_count += 1
        winning_count += 1
        print "You are alive."


while True:
    status = 1
    print "Winning : %d" % winning_count
    print "Played : %d" % played_count
    while status > 0:
        bomb()
