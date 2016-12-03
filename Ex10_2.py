fname = input('Enter a file name: ')
if len(fname) < 1:
	fname = 'mbox-short.txt'
fhand = open(fname)
hcount = dict()
hlist = list()
for line in fhand:
	if line.startswith('From'):
		line = line.split()
	if line[0] == ('From'):
		time = line[5]
		hour = time[0:2]
		hcount[hour] = hcount.get(hour,0) + 1
		
for hour,num in (hcount.items()):
	hlist.append((hour,num))
	hlist.sort()
	
for hour,num in hlist:
	print (hour,num)