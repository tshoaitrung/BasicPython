### defined 6 symbols for Tic Tac Toe: star,triangle,square,X,cricle and hexagon
def symbolTT(num):
    Symbol = ['⚝', '▲', '■', 'X','○','⬣']
    return Symbol[num]

### print the broad game 
def print_broad(broad_matrix):
    # print the broad in screen with the updated from player
    for i in broad_matrix:
        print('\t' + ''.join(i)) #''.join() is the function to convert the list to string

### choosing symbol for each player
def player_choose_symbol(number_player = 2):
    #we have two player so we have a list with 2 tuples:[(player_1,symbol),(player2,symbol)]
    result = []
    #Insert symbol for two players:
    symbol_temp = []
    print('\nWe have 6 symbols for tic tac toe game:')
    print('star (0): ' + symbolTT(0) + '\ttriangle(1): ' + symbolTT(1) + '\tsquare(2): '+ symbolTT(2) + '\tX(3): ' + symbolTT(3) + '\tcricle(4): ' + symbolTT(4) + '\thexagon(5): ' + symbolTT(5)) 
    for player in range(0,number_player,1):
        flag = False # flag the symbol is choose correct or not
        while flag == False:
            tmp = input('\nPlayer {} please choose a number corresponding to your symbol: '.format(player+1))
            if (not tmp in symbol_temp) and tmp.isdigit():
                if int(tmp) > 5:
                    print('!!!Out of range, please choose a number from 0 to 5!')
                else:
                    flag = True
                    print('\tThe symbol you choose is ' + symbolTT(int(tmp)))
            else:
                print('!!!you choose incorrect format or that symbol is chosen. Please choose again!')
        symbol_temp.append(tmp)
        result.append((player,int(tmp)))
    return result

### Decide the next game.
def continue_game():
    # ask player want a new game or not
    choice = 'wrong'
    while choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n':
        choice = input('Do you want the new game? Choose Y or N: ')
    if choice == 'Y' or choice == 'y':
        print('\nGREAT, THE NEW GAME WILL START NOW')
        return True
    else:
        print('\tGOODBYE')
        return False

### Check the current player win or not
def check_win(index,player):
    # check after the lastest step, who will be win
    if index[0][2] == index[1][2] == index[2][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
        
    if index[3][2] == index[4][2] == index[5][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
    
    if index[6][2] == index[7][2] == index[8][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
        
    if index[0][2] == index[3][2] == index[6][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
        
    if index[1][2] == index[4][2] == index[7][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
    
    if index[2][2] == index[5][2] == index[8][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
        
    if index[0][2] == index[4][2] == index[8][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
        
    if index[2][2] == index[4][2] == index[6][2]:
        print('\n\tCongrat! Player {} win this game'.format(player))
        return True
    return False

### Player choosing in each step
def player_choosing(player,index_marking):
    # update every step of player 
    choice = 'wrong'
    within_range = False
    position = False
    while choice.isdigit() == False or within_range == False or position == False:
        choice = input('Player {} please choose your number (1-9): '.format(player) )
        if choice.isdigit() == False: #digit check
            print('!!!Sorry that is not a digit, please choose again')
        else:
            if 1<= int(choice)<=9:#range check
                within_range = True
                if type(index_marking[int(choice)-1][2]) == int:# avaible position check
                    position = True
                else:
                    print('!!!This position is chosen, please choose again')
            else:
                print('!!!Out of range, please choose again with a digit from 1 to 9')
    return (int(choice)-1)
