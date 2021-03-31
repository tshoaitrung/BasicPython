###card game call "WAR"
#### to construct this game, we will create:
##### card class, player class and game logic
import random
from time import sleep
from Card_desk import *

class Card():
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
    
    def __str__(self):
        return f"{self.suit} and {self.number}"

class Player():
    def __init__(self, name, list_card=[]):
        self.name = name
        self.list_card = list_card
    
def game_rule(card1,card2):
    #return 0 - was case, 1- player 1 winthis turn, 2 player 2 win this turn
    if card1.number > card2.number:
        return 1
    elif card1.number < card2.number:
        return 2
    return 0
    
##################################MAIN##################################
sleep_time = 0.2
total_card = 52 #total 52 cards in a set with 4 suited and number from 1 to 10 and J,Q,k responding to 11,12,13
suit = [0,1,2,3]
number = list(range(1,14,1))

conti = 'Y' # continue with new game or not
while conti == 'Y':
    list_card_full = []
    for i in suit:
        for j in number:
            list_card_full.append(Card(i,j))

    random.shuffle(list_card_full) #dealing card
           
    print('\t\t\tLET START THE WAR CARD GAME\n')
    name1 = input('INSERT THE NAME OF PLAYER 1: ')
    player1 = Player(name1,list_card_full[0:26])

    name2 = input('INSERT THE NAME OF PLAYER 2: ')
    player2 = Player(name2,list_card_full[26:52])

    print('\nCARD DEALING: EACH PLAYER WILL HAVE 26 CARDS')
    print_double_back(player1.name,player2.name)
    sleep(sleep_time)
    turn = 0
    endgame = False
    while endgame == False:
        turn +=1
        print ('\n\t\tTURN {}:'.format(turn))
        print_double(player1.name,len(player1.list_card),player1.list_card[0].suit,player1.list_card[0].number, player2.name,len(player2.list_card),player2.list_card[0].suit,player2.list_card[0].number)
        sleep(sleep_time)
        result_turn = game_rule(player1.list_card[0], player2.list_card[0])
        if result_turn == 1: # the player 1 win this turn so the player 1 need keep both cards
            print('\tPLAYER 1 WON THIS TURN')
            pop_card1 = player1.list_card.pop(0)
            pop_card2 = player2.list_card.pop(0)
            player1.list_card.append(pop_card1)
            player1.list_card.append(pop_card2)
            if len (player2.list_card) == 0:
                print('### CONGRAT PLAYER 1 - YOU ARE THE NEW WINNER ###')
                endgame = True
        elif result_turn == 2: #the player 2 win this turn so the player 1 need to keep both cards
            print('\tPLAYER 2 WON THIS TURN')
            pop_card1 = player1.list_card.pop(0)
            pop_card2 = player2.list_card.pop(0)
            player2.list_card.append(pop_card2)
            player2.list_card.append(pop_card1)
            if len (player1.list_card) == 0:
                print('### CONGRAT PLAYER 2 - YOU ARE THE NEW WINNER ###')
                endgame = True
        else: ### the war happends in this turn
            print('\t ###WAR - LET FLIGHT###')
            war_flag = True
            wait_list =[]
            pop_card1 = player1.list_card.pop(0)
            pop_card2 = player2.list_card.pop(0)
            wait_list.append(pop_card1)
            wait_list.append(pop_card2)
            while war_flag == True:
                print('TOTAL CARD IN WAITING LIST IS {} to wait the winner of this was'.format(len(wait_list)))
                if len(player1.list_card) < 4: # if player 1 dont have enough 4 card for fighting
                    print('PLAYER 1 YOU DONT HAVE ENOUGH 4 CARDS TO WAR. YOU LOOSE THIS GAME')
                    print('### CONGRAT PLAYER 2 - YOU ARE THE NEW WINNER ###')
                    endgame = True
                    war_flag = False
                elif len(player2.list_card) < 4: #if play 2 dont have enough 4 card for fighting
                    print('PLAYER 2 YOU DONT HAVE ENOUGH 4 CARDS TO WAR. YOU LOOSE THIS GAME')
                    print('### CONGRAT PLAYER 1 - YOU ARE THE NEW WINNER ###')
                    endgame = True
                    war_flag = False
                else:
                    index = 0
                    for index in range (3): # take out 3 cards and put in wait_ list and wait the decision from the 4th cards.
                        pop_card1 = player1.list_card.pop(0)
                        pop_card2 = player2.list_card.pop(0)
                        wait_list.append(pop_card1)
                        wait_list.append(pop_card2)
                    print('DISTRIBUTE THREE TOP CARDS AND LET COMPARE THE 4TH CARD')
                    print_double(player1.name,len(player1.list_card),player1.list_card[0].suit,player1.list_card[0].number, player2.name,len(player2.list_card),player2.list_card[0].suit,player2.list_card[0].number)
                    sleep(sleep_time)
                    result_turn = game_rule(player1.list_card[0], player2.list_card[0])
                    if result_turn == 1: # the player 1 win this war
                        war_flag = False
                        for temp_card in wait_list:
                            player1.list_card.append(temp_card)
                        pop_card1 = player1.list_card.pop(0)
                        pop_card2 = player2.list_card.pop(0)
                        player1.list_card.append(pop_card1)
                        player1.list_card.append(pop_card2)
                        if len (player2.list_card) == 0:
                            print('### CONGRAT PLAYER 1 - YOU ARE THE NEW WINNER ###')
                            endgame = True
                    elif result_turn == 2: #the player 2 win this war
                        war_flag = False
                        for temp_card in wait_list:
                            player2.list_card.append(temp_card)
                        pop_card1 = player1.list_card.pop(0)
                        pop_card2 = player2.list_card.pop(0)
                        player2.list_card.append(pop_card1)
                        player2.list_card.append(pop_card2)
                        if len (player1.list_card) == 0:
                            print('### CONGRAT PLAYER 1 - YOU ARE THE NEW WINNER ###')
                            endgame = True
    conti = ''
    while conti !='Y' and conti !='N':
        conti = input('\n DO YOU WANT A NEW GAME (Y/N ONLY): ')

print('\n\t\tTHANK YOU PLAY GAME WITH US! GOOGBYE!')
           