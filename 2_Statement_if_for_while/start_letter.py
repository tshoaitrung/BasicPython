### Date: March, 16th, 2021
#### Some example code about Python Statement ( if, for, while)
#1. Print out the words in string that starts with the letter you want

print("Print out the words in string that starts with the letter you want\n")
IP_Str = input("Insert the String to check: ")
Letter_need = input("Insert the letter the words should started with: ")
Proc_Str = IP_Str.split()
count = 0 # counting total of words start with Letter_need
index = 0 # to print the position of words

for words in Proc_Str :
	if words[0] == Letter_need.upper() or words[0] == Letter_need.lower() :
		count += 1
		print('At index {} the words start with {} is {}'.format(index, Letter_need, words))
	index += 1

if count > 0 :
	print('\nTotal words are printed is {}'.format(count))
else:
	print('No word in your string start with {}'.format(Letter_need))
