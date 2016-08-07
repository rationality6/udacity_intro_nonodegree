# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

#
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"


def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location != True:
        return somestring
    print location
    length = len(sub)
    print length

    part_before = somestring[:location]
    print part_before + ' 1'
    part_after = somestring[location + length:]
    print part_after + ' 2'
    return part_before + part_after

#
# Don't change these test cases!
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
