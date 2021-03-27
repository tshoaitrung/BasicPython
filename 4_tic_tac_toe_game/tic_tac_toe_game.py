### Create a Tic Tac Toe game for 2 human
#The broad of this game withh be like that
#
# 1 | 2 | 3
#---|---|---
# 4 | 5 | 6 
#---|---|---
# 7 | 8 | 9
#
### This program includes 5 small functions
def print_broad(broad_matrix):
    # print the broad in screen with the updated from player
    for i in broad_matrix:
        print(''.join(i)) #''.join() is the function to convert the list to string
        
def play_choose_symbol():
    # for they player choosing X or O to play the game.
    player_1 = ''
    while player_1 == '':
        player_1 = input('Player 1 please choose X or O is yours: ')
        if player_1 != 'X' and player_1 != 'O':
            player_1 = ''
            print('Choose wrong! please do again')
    if player_1 =='X':
        print('The player 1 chooses X and player 2 choose O')
        return [player_1,'O']
    else:
        print('The player 1 chooses O and player 2 choose X')
        return [player_1,'X']

    
def player_choosing(player,index_marking):
    # update every step of player 
    choice = 'wrong'
    within_range = False
    position = False
    while choice.isdigit() == False or within_range == False or position == False:
        choice = input('Player {} please choose your number (1-9): '.format(player) )
        if choice.isdigit() == False: #digit check
            print('Sorry that is not a digit, please choose again')
        else:
            if 1<= int(choice)<=9:#range check
                within_range = True
                if type(index_marking[int(choice)-1][2]) == int:# avaible position check
                    position = True
                else:
                    print('This position is chosen, please choose again')
            else:
                print('Out of range, please choose again with a digit from 1 to 9')
    return (int(choice)-1)
        
    
def check_win(index,player):
    # check after the lastest step, who will be win
    if index[0][2] == index[1][2] == index[2][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
        
    if index[3][2] == index[4][2] == index[5][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
    
    if index[6][2] == index[7][2] == index[8][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
        
    if index[0][2] == index[3][2] == index[6][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
        
    if index[1][2] == index[4][2] == index[7][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
    
    if index[2][2] == index[5][2] == index[8][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
        
    if index[0][2] == index[4][2] == index[8][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
        
    if index[2][2] == index[4][2] == index[6][2]:
        print('Congrat! Player {} win this game'.format(player))
        return True
    return False
    
def continue_game():
    # ask player want a new game or not
    choice = 'wrong'
    while choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n':
        choice = input('Do you want the new game? Choose Y or N: ')
    if choice == 'Y' or choice == 'y':
        print('---LET START A NEW GAME---')
        return True
    else:
        print('GOODBYE')
        return False
    
#######################MAIN################################
###The tic tac toe game for two players
## The maximum steps total is 9
print('Let play the TIC TOC TOE GAME')
is_playing = True
while is_playing == True:
    #set up a new game
    print ('PERFECT LET PLAY OUR TIC TOC TOE GAME')
    print('The broad of this game: ')
    print("For each step, please choose the number coresponding to the space (as the you want to put your 'x' or 'o'")
    index_marking = [[0,1,1], [0,5,2], [0,9,3], [2,1,4], [2,5,5], [2,9,6], [4,1,7], [4,5,8], [4,9,9]] # save the location of symbol and step of players
    broad_matrix = [[' ','1',' ','|',' ','2',' ','|',' ','3',' '],['-','-','-','|','-','-','-','|','-','-','-'],[' ','4',' ','|',' ','5',' ','|',' ','6',' '],['-','-','-','|','-','-','-','|','-','-','-'],[' ','7',' ','|',' ','8',' ','|',' ','9',' ']]#saving the current broad to display on the screen
    print_broad(broad_matrix)
    player_symbol = play_choose_symbol()
    #start a game
    num_step = 0 #maximum step  = 8
    win = False # check win or not to finish the game
    
    while num_step < 9 and win == False:
        step = player_choosing(num_step%2+1,index_marking)#num_step%2+1 use to defind which players turn, num_step%2+1 = 1 or 2 coresponding to player 1 and 2
        index_marking[step][2] = player_symbol[num_step%2]
        broad_matrix[index_marking[step][0]][index_marking[step][1]] = player_symbol[num_step%2]
        print_broad(broad_matrix)
        win = check_win(index_marking,num_step%2+1)
        num_step += 1
    
    if win == False:
        print('THE GAME IS END, NO ONE WIN THIS GAME')
        
    is_playing = continue_game()
