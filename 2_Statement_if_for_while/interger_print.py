#3. Prints the interger from 1 to 100. But for multiples of 3 print "great333", for multiples of 5 print "great555", for the both multuples of 3 and 5 print "great333555"
print('Prints the interger from 1 to 100. But for multiples of 3 print "great333", for multiples of 5 print "great555", for the both multuples of 3 and 5 print "great333555"\n');

for num in range (1,101,1):
	if num % 3 == 0:
		if num % 5 == 0:
			print('great333555')
		else:
			print('great333')
	elif num % 5 == 0:
		if num % 3 == 0:
			print('great333555')
		else:
			print('great555')
	else:
		print(num)

