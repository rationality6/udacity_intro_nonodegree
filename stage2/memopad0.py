def is_friend(n):
	if 'D' == n[0] or 'N' ==n[0]:
		return True
	else:
		return False
print is_friend('Diane')
print is_friend('Ned')
print is_friend('Moe')

def biggest(a,b,c):
	if a>b:
		if a>c:
			return a
		else:
			return c
	else:
		if b>c:
			return b
		else:
			return c

print biggest(2,2,1)


def bigger(a,b):
	if a>b:
		return a
	else:
		return b

def biggest(a,b,c):
	return bigger(bigger (a,b),c)

print bigger(3,2)
print biggest(3,2,1)

i = 1
while i != 10:
	i = i + 2
	print i



i = 0
while i < 10:
    print i
    i = i+1



def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
	# print text
    return text_without_spaces

print remove_spaces("hello my name is andy how are you?")

def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]

		if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]

    return text_without_spaces

print remove_spaces("hello my name is andy how are you?")

def print_numbers(i):
	n = 0
	while n <= i:
		n = n+1
		print n

print_numbers(0)

n=5
i=1
while True:
	if i > n:
		break
	print i
	i = i + 1

def print_numbers(n):
	i=0
	while i<=n:
		print i
		i=i+1
print_numbers(5)
