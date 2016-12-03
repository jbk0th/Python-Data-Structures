fname = input('Enter a file name: \n')
if fname == 'na na boo boo':
	print("NA NA BOO BOO TO YOU - You have been punk'd!")
fhandle = open(fname,'r')
for line in fhandle:
	print (line.upper())