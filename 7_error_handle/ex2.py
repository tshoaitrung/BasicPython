Handle the exception thrown using try and except 
"""
x = 5
y = 0
z = x/y
"""
conti = 'Y'
while conti =='Y' or conti =='y':  
    while True:
        try:
            dividend_Input = input('Insert a dividend (a): ')
            dividend = int (dividend_Input)
            break
        except:
            print('WRONG TYPE, PLEASE DO AGAIN')

    while True:
        try:
            divisor_Input = input('Insert a divisor (b): ')
            divisor = int (divisor_Input)
            break
        except:
            print('WRONG TYPE, PLEASE DO AGAIN')
            
    try:
        t = float(dividend/divisor)
        print('THE RESULT OF DIVISON OPERATOR a/b is: {}'.format(t))
    except:
        print('THE OPERATOR COULD NOT COMPLETED BECAUSE DIVISOR = 0')
    
    conti = input('Do you want to continue(y/n): ')
    
