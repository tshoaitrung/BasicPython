#####visualize for card desk
######clubs: like a tree and black
######Diamonds: like diamions and red
######Hearts: like heart and red
######Spades: reversve heat and black
#####Orders: spades < clubs < diamonds < hearts

def frame():
    row = 12
    col =  10
    result = []
    for i in range(0,row,1):
        tmp =[]
        if i == 0 or i == (row-1):
            for j in range (0,col,1):
                tmp.append('-')
        else:
            tmp.append('|')
            for j in range (1,col-1,1):
                tmp.append(' ')
            tmp.append('|')
        result.append(tmp);
    return result
    
def card_value(nums):
    #value from 1 to 13: 11 is J, 12 is Q and 13 is K
    result = []
    if nums == 1:
        result = [[' ',' ','*','*',' ',' '],[' ','*','*','*',' ',' '],['*','*','*','*',' ',' '],[' ',' ','*','*',' ',' '],[' ',' ','*','*',' ',' '],[' ',' ','*','*',' ',' '],['*','*','*','*','*','*'],['*','*','*','*','*','*']]
    elif nums == 2:
        result = [[' ','*','*','*',' ',' '],['*','*','*','*','*',' '],['*','*',' ',' ','*','*'],[' ',' ',' ','*','*','*'],[' ',' ','*','*','*',' '],[' ','*','*',' ',' ',' '],['*','*','*','*','*','*'],['*','*','*','*','*','*']]
    elif nums == 3:
        result = [[' ','*','*','*','*',' '],['*','*','*','*','*','*'],[' ',' ',' ',' ','*','*'],[' ',' ',' ','*','*',' '],[' ',' ',' ','*','*',' '],[' ',' ',' ',' ','*','*'],['*','*','*','*','*','*'],[' ','*','*','*','*',' ']]
    elif nums == 4:
        result = [['*','*',' ',' ',' ',' '],['*','*',' ',' ',' ',' '],['*','*',' ',' ','*','*'],['*','*','*','*','*','*'],[' ','*','*','*','*','*'],[' ',' ',' ',' ','*','*'],[' ',' ',' ',' ','*','*'],[' ',' ',' ',' ','*','*']]
    elif nums == 5:
        result = [['*','*','*','*','*','*'],['*','*','*','*','*','*'],['*','*',' ',' ',' ',' '],['*','*','*','*',' ',' '],['*','*','*','*','*',' '],[' ',' ',' ',' ','*','*'],[' ',' ',' ',' ','*','*'],['*','*','*','*','*',' ']]
    elif nums == 6:
        result = [[' ','*','*','*','*',' '],['*','*','*','*','*','*'],['*','*',' ',' ','*','*'],['*','*',' ',' ',' ',' '],['*','*','*','*','*',' '],['*','*',' ',' ','*','*'],['*','*',' ',' ','*','*'],[' ','*','*','*','*',' ']]
    elif nums == 7:
        result = [['*','*','*','*','*','*'],['*','*','*','*','*','*'],[' ',' ',' ',' ','*','*'],[' ',' ',' ',' ','*','*'],[' ',' ',' ','*','*',' '],[' ',' ','*','*',' ',' '],[' ','*','*',' ',' ',' '],['*','*',' ',' ',' ',' ']]
    elif nums == 8:
        result = [[' ',' ','*','*',' ',' '],[' ','*',' ',' ','*',' '],[' ','*',' ',' ','*',' '],[' ',' ','*','*',' ',' '],[' ','*',' ',' ','*',' '],['*',' ',' ',' ',' ','*'],['*',' ',' ',' ',' ','*'],[' ','*','*','*','*',' ']]
    elif nums == 9:
        result = [[' ','*','*','*','*',' '],['*','*',' ',' ','*','*'],['*','*',' ',' ','*','*'],[' ','*','*','*','*','*'],[' ',' ',' ',' ','*','*'],['*','*',' ',' ','*','*'],['*','*','*','*','*','*'],[' ','*','*','*','*',' ']]
    elif nums == 10:
        result = [['*',' ',' ','*','*',' '],['*',' ','*',' ',' ','*'],['*',' ','*',' ',' ','*'],['*',' ','*',' ',' ','*'],['*',' ','*',' ',' ','*'],['*',' ','*',' ',' ','*'],['*',' ','*',' ',' ','*'],['*',' ',' ','*','*',' ']]
    elif nums == 11:
        result = [[' ','*','*','*','*',' '],['*','*','*','*','*','*'],[' ',' ',' ','*','*',' '],[' ',' ',' ','*','*',' '],[' ',' ',' ','*','*',' '],['*','*',' ','*','*',' '],['*','*','*','*',' ',' '],[' ','*','*',' ',' ',' ']]
    elif nums == 12:
        result = [[' ',' ','*','*',' ',' '],[' ','*','*','*','*',' '],['*','*',' ',' ','*','*'],['*','*',' ',' ','*','*'],['*','*',' ',' ','*','*'],['*','*',' ','*','*','*'],[' ','*','*','*','*',' '],[' ',' ','*','*','*','*']]
    elif nums == 13:
        result = [['*','*',' ',' ','*','*'],['*','*',' ','*','*',' '],['*','*','*','*',' ',' '],['*','*','*',' ',' ',' '],['*','*','*',' ',' ',' '],['*','*','*','*',' ',' '],['*','*',' ','*','*',' '],['*','*',' ',' ','*','*']]
    elif nums == 0: #backside
        result = [[' ',' ','*','*',' ',' '],[' ','*',' ',' ','*',' '],[' ','*',' ',' ',' ','*'],[' ',' ',' ',' ',' ','*'],[' ',' ',' ',' ','*',' '],[' ',' ',' ','*',' ',' '],[' ',' ','*',' ',' ',' '],[' ',' ','*',' ',' ',' ']]
    return result
    
def print_card(suit_value = 0,value = 0):
    #heart = 0, diamons = 1,spade = 2, club = 3
    suit = '♥♦♣♠'
    card = frame()
    number = card_value(value)
    tmp = 0
    for index,row in enumerate(cards):
        if index == 1:
            row[1] = suit[suit_value]
            print(''.join(row))
        elif index == (len(cards)-2):
            row[-2] = suit[suit_value]
            print(''.join(row))
        elif index >=2 and index <=9:
            for j in range(len(number[0])):
                row[j+2] = number[tmp][j]
            tmp += 1
            print(''.join(row))
        else:
            print(''.join(row))  

def print_double(name1 = '',total1 = 26,suit_value1 = 0,value1 = 0,name2 ='',total2 = 26,suit_value2 = 0,value2 = 0):
    suit = '♥♦♣♠'
    card1 = frame()
    card2 = frame()
    number1 = card_value(value1)
    number2 = card_value(value2)
    distance = '\t\t\t '
    #the distance between two players is 3 tab
    print('PLAYER 1: ' + name1 + distance + 'PLAYER 2: ' + name2)
    print('TOTAL: {} cards'.format(total1) + distance + 'TOTAL: {} cards'.format(total2))
    tmp = 0
    for index in range(len(card1)):
        if index == 1:
            card1[index][1] = suit[suit_value1]
            card2[index][1] = suit[suit_value2]
            print(''.join(card1[index]) + distance + ''.join(card2[index]))
        elif index == (len(card1)-2):
            card1[index][-2] = suit[suit_value1]
            card2[index][-2] = suit[suit_value2]
            print(''.join(card1[index]) + distance + ''.join(card2[index]))
        elif index >=2 and index <=9:
            for j in range(len(number1[0])):
                card1[index][j+2] = number1[tmp][j]
                card2[index][j+2] = number2[tmp][j]
            tmp += 1
            print(''.join(card1[index]) + distance + ''.join(card2[index]))
        else:
            print(''.join(card1[index]) + distance + ''.join(card2[index]))

def print_double_back(name1, name2, total1 = 26, total2=26):
    card1 = frame()
    card2 = frame()
    number = card_value(0) #backside
    distance = '\t\t\t '
    #the distance between two players is 3 tab
    print('PLAYER 1: ' + name1 + distance + 'PLAYER 2: ' + name2)
    print('TOTAL: {} cards'.format(total1) + distance + 'TOTAL: {} cards'.format(total2))
    tmp = 0
    for index in range(len(card1)):
        if index >=2 and index <=9:
            for j in range(len(number[0])):
                card1[index][j+2] = number[tmp][j]
                card2[index][j+2] = number[tmp][j]
            tmp += 1
            print(''.join(card1[index]) + distance + ''.join(card2[index]))
        else:
            print(''.join(card1[index]) + distance + ''.join(card2[index]))
            
#print_double_back('a','b')