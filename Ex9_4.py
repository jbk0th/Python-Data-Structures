import string

# = str.maketrans({key:None for key in string.punctuation})

fname = input('Enter a filename: ')
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
adcount = dict()
for line in fhand:
#	line = line.translate(translator)
	if line.startswith('From'): #check if the line starts with From
		line = line.split() #splits the string into a list, with spaces as th boundaries
		if line[0] == 'From': #check if the first element is From and not From:
			adcount[line[1]] = adcount.get(line[1],0) + 1 #returns the value from the key provided if its in the dictionary, if not returns the provided defualt value
		
values = adcount.values()
largest = None
email = None
for key in adcount:
	if largest == None or adcount.get(key,0) > largest :
		largest = adcount.get(key,0)
		email = key

print(email, largest)