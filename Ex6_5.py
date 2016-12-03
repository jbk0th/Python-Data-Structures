str = 'X-DSPAM-Confidence: 0.8475'
sppos = str.find('0')
fivepos = str.find('5')
print (fivepos)
deci_num = str[sppos:fivepos+1]
floating_deci = float(deci_num)
print (floating_deci)
