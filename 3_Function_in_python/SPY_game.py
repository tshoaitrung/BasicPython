### SPY_Game: write a function in the list of interger and return true if it contains 007 in order
### example [1,2,0,0,7] return true [0,54,565,0,7] true 

def input_list():
	
	print ('Start insert your list ( type any letter (not number to stop)): ')
	try:
		result = []
		while True:
			result.append(int(input()))
	except:
		return result
	

def search_in_list(IP_list,SPY_list):
	flag = 0
	if len(IP_list)<len(SPY_list) :
		return False
	else :
		for num in IP_list:
			if flag == len(SPY_list):
				return True
			else:
				if num == SPY_list[flag] :
					flag += 1
	
	if flag == len(SPY_list) and flag > 0:
		return True
	return False

####---MAIN---####
print ('SPY_Game: write a function in the list of interger and return true if it contains 007 in order\n')
print('Insert your list of interger input: ')
IP_list = input_list()

print('Insert your SPY_list: ')
SPY_list = input_list()

RESULT = search_in_list(IP_list,SPY_list)

print ('your INPUT list is: ')
print (IP_list)
print ('your SPY list is: ')
print (SPY_list)

if RESULT == True:
	print('TRUE: your SPY_list is in your INPUT_list')
else:
	print('FALSE: your SPY_list is not in your INPUT_list')

