###Handle the exception thrown by the code below by using try and except block 
"""for i in ['a','b','c']
	print (i**2)"""

input_list = input('Insert the string: ')
for index in list(input_list):
    try:
        t = int(index)
        print('the square of this element ' + index + ' is {}'.format(t**2))
    except:
        print('This element is not a number')
