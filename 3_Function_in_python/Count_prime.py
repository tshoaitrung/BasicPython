### Function_ learning
###Count_prime: write a function that return the number of prime numbers that exist up to and including a given number
### Simple_prime is the popular why to check a number is prime or not
### Fast_prime is the better algorithm to find all prime numbers in a list from 0 to giving number
def is_prime(n):
	if n == 0 or n == 1:
		return False
	elif n == 2 or n == 3:
		return True
	else:
		for num in range(2,n,1):
			if n%num == 0:
				return False
		return True


def simple_prime(n):
	result = []
	for num in range(n+1):
		if is_prime(num):
			result.append(num)

	return result

def fast_prime(n):
	marker_list = [0] * (n+1)
	marker_list[0] = 1
	marker_list[1] = 1
	result =[];
	for num in range(n+1):
		if marker_list[num] == 0:
			result.append(num)
			tmp = num + num
			while(tmp<=n):
				marker_list[tmp] = 1
				tmp = tmp + num

	return result

###---MAIN---###
print('Count_prime: write a function that return the number of prime numbers that exist up to and including a given number')

INPUT = int(input('Insert your number: '))

result1 = simple_prime(INPUT)
result2 = fast_prime(INPUT)

print('Simple Method: total ' + str(len(result1)) + ' prime numbers')
print(result1)
	
print('Fast Method: total ' + str(len(result2)) + ' prime numbers')
print(result2)
