### Create a Tic Tac Toe game for 2 human
#The broad of this game withh be like that
#
# 1 | 2 | 3
#---|---|---
# 4 | 5 | 6 
#---|---|---
# 7 | 8 | 9
#
from symbol_rule import *
    
#######################MAIN################################
###The tic tac toe game for two players
## The maximum steps total is 9
print('\n\tWELCOME TO TIC TAC TOE GAME')
is_playing = True
while is_playing == True:
    #set up a new game
    print ('\n\t START A NEW GAME')
    print('\tThe broad of this game: ')
    print("For each step, please choose the number coresponding to the space")
    index_marking = [[0,1,1], [0,5,2], [0,9,3], [2,1,4], [2,5,5], [2,9,6], [4,1,7], [4,5,8], [4,9,9]] # save the location of symbol and step of players
    broad_matrix = [[' ','1',' ','|',' ','2',' ','|',' ','3',' '],['-','-','-','|','-','-','-','|','-','-','-'],[' ','4',' ','|',' ','5',' ','|',' ','6',' '],['-','-','-','|','-','-','-','|','-','-','-'],[' ','7',' ','|',' ','8',' ','|',' ','9',' ']]#saving the current broad to display on the screen
    print_broad(broad_matrix)
    player_symbol = player_choose_symbol()
    print('\n The player 1 choose : ' + symbolTT(player_symbol[0][1]) + '\t and player 2 choose: ' + symbolTT(player_symbol[1][1]))
    print('\n\t GAME STARTS NOW')
    #start a game
    num_step = 0 #maximum step  = 8
    win = False # check win or not to finish the game
    
    while num_step < 9 and win == False:
        step = player_choosing(num_step%2+1,index_marking)#num_step%2+1 use to defind which players turn, num_step%2+1 = 1 or 2 coresponding to player 1 and 2
        index_marking[step][2] = symbolTT(player_symbol[num_step%2][1])
        broad_matrix[index_marking[step][0]][index_marking[step][1]] = symbolTT(player_symbol[num_step%2][1])
        print_broad(broad_matrix)
        win = check_win(index_marking,num_step%2+1)
        num_step += 1
    
    if win == False:
        print('\n\tTHE GAME IS END, NO ONE WIN THIS GAME')
        
    is_playing = continue_game()
