import string
#Create dictionary using a comprehension - this maps every character from sting.punctuation to None.
# Initializse a translation object from it.
num = '0123456789'
translator = str.maketrans({key:None for key in string.punctuation})
translatornum = str.maketrans({key:None for key in num})

fname = input('Enter a file name: ')
if len(fname) < 1:
	fname = 'mbox-short.txt'
fhand = open(fname)
ltrcount = dict()
chrlist = list()
for line in fhand:
	line = line.translate(translator)
	line = line.translate(translatornum)
	line = line.lower()
	words = line.split()
	for word in words:
		for char in word:
			ltrcount[char] = ltrcount.get(char,0) + 1
			
for letter,count in (ltrcount.items()):
	chrlist.append((count,letter))
	chrlist.sort()
	
for num,chr in chrlist:
	print(chr,num)


