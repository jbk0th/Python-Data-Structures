fname = input('Enter a filname: ')
fhand = open(fname)
counts = dict()
for line in fhand:
	line = line.split()
	for element in line:
		counts[element] = 1

print(counts)