# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day.find('Saturday') and day.find('Sunday'):
        return False
    else:
        return True

print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

print weekend('Sunday')
#>>> False


def countdown(c):
    i = 0
    while i < c:
        print c
        c = c-1
    print 'Blastoff!'
countdown(3)
