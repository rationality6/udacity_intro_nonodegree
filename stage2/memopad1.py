
# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')

def printInches(n):
    print str(n) + " inches"

printInches(42)

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text):
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')
print 'a'
