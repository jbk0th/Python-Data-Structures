def countit(str_var,letter):
	count_var = 0
	for char in str_var:
		if char == letter:
			count_var = count_var + 1
	print(count_var)
	return count_var


word = 'banana'
letter = 'a'

countit(word,letter)