fhand = open('mbox-short.txt')
list_var = list()
count = 0
for line in fhand:
	list_var = line.split()
	print(list_var)
	if len(list_var) > 1 and list_var[0] == ('From'):
		count = count + 1
		list_var = line.split()
		print(list_var[1])

print('There were',count,'lines with From as the first word')
	