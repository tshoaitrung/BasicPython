### Write a Python function to check whether a string is pangram or not
# Pangrams are words or sentences containning every letter of the alphabet at least once
print ('Write a Python function to check whether a string is pangram or not')

def UPPER_detect(num):
    if 65<= num <= 90:#UPCASE LETTER RANGE
        return True
    return False  
    
def index_return(letter):
    num = ord(letter)
    if UPPER_detect(num):
        return (num-65)
    return (num-97)

INPUT = input('Insert your string to check it is pangram or not: ')
alphabet_list = [0]* 26 #(26 letters)
for letter in INPUT:
    index = index_return(letter)
    if 0<= index <26:
        alphabet_list[index] = 1

if sum(alphabet_list) == 26:
    print('Your string is pangram')
else:
    print('Your string is NOT pangram')

