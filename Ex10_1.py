fname = input('Enter a file name: ')
fhand = open(fname)
adcount = dict()
for line in fhand:
	if line.startswith('From'):
		line = line.split()
	if line[0] == ('From'):
		print(line)
		address = line[1]
		adcount[address] = adcount.get(address,0) + 1
	
comlist = list()
for address,count in (adcount.items()): #returns a list of tuples for each key,value pair in the list
	comlist.append((count,address)) #iterate over the pair of address, and count at a time, switch thir posit
	comlist.sort(reverse = True) #ordering in the list to sort by counts, the sort h - l
	
print(comlist[0])
	