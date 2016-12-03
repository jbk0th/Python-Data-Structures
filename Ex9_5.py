import string

# = str.maketrans({key:None for key in string.punctuation})

fname = input('Enter a filename: ')
fhand = open(fname)
domcount = dict()
i = 0

for line in fhand:
#	line = line.translate(translator)
	if line.startswith('From'): #check if the line starts with From
		line = line.split() #splits the string into a list, with spaces as th boundaries
		if line[0] == 'From': #check if the first element is From and not From:
			email = line[1]
			atpos = email.find('@')
			domcount[email[atpos:]] = domcount.get(email[atpos:],0) + 1

print(domcount)			
			
