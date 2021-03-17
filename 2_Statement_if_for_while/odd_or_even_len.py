#2. Print out the words if the length of word is even, print out the reverse of words if the length of word is odd
### ODD NUMBER x%2 == 1 vs EVEN NUMBER x%2 == 0
print("Print out the words if the length of word is even, print out the reverse of words if the length of word is odd\n")
IP_Str = input("Insert the String you want: ")
Proc_Str = IP_Str.split()
count_EV = 0
count_OD = 0

for words in Proc_Str :
	if len(words)%2 == 0 :
		count_EV += 1
		print('The length of {} is even'.format(words))
	else:
		count_OD += 1
		print('\tThe length of {} is odd and the reverse is {}.'.format(words,words[::-1]))

print('\nTOTAL WORDS IN YOUR STRING HAVE EVEN LENGTH IS {}. '.format(count_EV))
print('TOTAL WORDS IN YOUR STRING HAVE ODD LENGTH IS {}.'.format(count_OD))
