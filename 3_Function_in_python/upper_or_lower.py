### Write a Python function that accepts a string and calculates the number of upper letters and lower letters
## Using map OR filter function not using isupper() function
print('Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters')

def UPPER_detect(letter):
    if 65<= ord(letter)<= 90:#UPCASE LETTER RANGE
        return True
    return False
 
def LOWER_detect(letter):
    if 97<= ord(letter)<= 122: #LOWERCASE LETTER RANGE
        return True
    return False

INPUT = input ('Insert your string to calculate the number of upper case letters and lower case letters: ')
LOWER = list(filter(LOWER_detect,INPUT))
print('The total of lower string is: {} with the return LOWER STRING is '.format(len(LOWER)))
print(LOWER)
UPPER = list(filter(UPPER_detect,INPUT))
print('The total of lower string is: {} with the return UPPER STRING is '.format(len(UPPER)))
print(UPPER)
