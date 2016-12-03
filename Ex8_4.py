fhand = open('romeo.txt')
uniq_words = list()
for line in fhand:
	line = line.rstrip()
	words = line.split()
	for element in words:
		if element not in uniq_words:
			uniq_words.append(element)
uniq_words.sort()
print(uniq_words)
	

