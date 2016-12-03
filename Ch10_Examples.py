import string
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	line.translate(string.punctuation)
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in words:
			counts[word] = 1
		else:
			counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in list(counts.items()):
	lst.append((val,key))
	
lst.sort(reverse = True)

for key, val in lst[:10]:
	print(key,val)