fname = input('Enter a file name: \n')
fh = open(fname,'r')
count = 0
total_conf = 0
for line in fh:
	if line.startswith('X-DSPAM-Confidence'):
		num_beg = line.find('0')
		#end = num_beg+6
		total_conf = total_conf + float(line[num_beg:])
		count = count + 1
ave = total_conf/count
print('Average spam confidence: ',ave)