num_list = list()
while (True):
	inp = input('Enter a number: ')
	if inp == 'done': break
	num_list.append(inp)
	
max_num = max(num_list)
min_num = min(num_list)
print('Maximum:',max_num)
print('Minimum:',min_num)
	