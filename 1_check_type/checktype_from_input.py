#Date: March, 13th, 2021
#The first project to understand basic type in Python such as, number ( interger or float), string, list and Booleans
#frist step: check the type of input
IPut = input ("Insert an input to check the type: ")
#the type of value from the input() function always returns string
print("The type of input is: ",type(IPut))
#Check the inout could be the interger or not and covert to interger
try:
    check_ising = int(IPut)
    print("The input could be the interger type")
except:
    print("The input could not be the interger type")
    try:
        check_isfl = float(IPut)
        print("The input could be the float type")
    except:
        print("The input could not be the float type")
