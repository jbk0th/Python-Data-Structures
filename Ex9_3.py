import string

# = str.maketrans({key:None for key in string.punctuation})

fname = input('Enter a filename: ')
fhand = open(fname)
adcount = dict()
for line in fhand:
#	line = line.translate(translator)
	if line.startswith('From'): #check if the line starts with From
		line = line.split() #splits the string into a list, with spaces as th boundaries
		if line[0] == 'From': #check if the first element is From and not From:
			adcount[line[2]] = adcount.get(line[2],0) + 1 #returns the value from the key provided if its in the dictionary, if not returns the provided defualt value
		
print(adcount)