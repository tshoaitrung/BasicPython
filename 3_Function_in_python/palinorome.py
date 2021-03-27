### Write a Python function that checks whether a word or pharse is palindrome or not
## Example if palindrome string is: dogod or kijjik
print('Write a Python function that checks whether a word or pharse is palindrome or not')

def is_palindrome(PHARSE):
    index = len(PHARSE)
    if index < 2:
        return False
    else:
        for i in range (0,int(index/2),1):
            if PHARSE[i] != PHARSE[index-1 -i]:
                return False
    return True

INPUT = input('Insert you words or pharse to check it is palinorome or not: ')
if is_palindrome(INPUT):
    print('Your input is palinorome!')
else:
    print('Your input is NOT palinorome!')

