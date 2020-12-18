#########################################################################
#file name :min_max_algorithm.py
#Description:
'''Tic-tac-toe (XO)
Tic-tac-toe is a simple game, but it can be used to illustrate the same minimax algorithm
that can be applied in advanced strategy games like Connect Four, checkers,
and chess. We will build a tic-tac-toe AI that plays perfectly using minimax.
'''
# Version     : 0.1  
# Author : Mohamed Reda
#
# 
##########################################################################  

########################  BOARD POSITIONS ################################
#                        |  1   |  2   |  3 |                          
#                       |______|______|_____|                         
#                      |  4   |  5   |   6 |
#                     |______|______|_____|                                   
#                     |  7  |  8   |    9  |                                   
#                    |______|______|______|                                     
## ########################################################################
##########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################      
def insertLetter(letter, pos):
    board[pos] = letter
#########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################    
def spaceIsFree(pos):
    return board[pos] == ' '
#########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################    
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
 #########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################       
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)
#########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################    
def playerMove():
    run = True
    while run:
        move = input('Select a position to place an \'X\'(1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Type a number within the range(1:9)!')
        except:
            print('!Are u Mad! Please Type a number!')
#########################################################################
#Description:this function responsable for check if the board postions 
#            empty or not .
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################               

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0  #intial steate

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move
#########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################    
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
#########################################################################
#Description:this function responsable for check if the board postions empy or not 
# INPUT:None
# OUTPUT:retrun True if full False if Empty
# 
##########################################################################     
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to My (XO) GAME . ')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('GOOD LUCK, Computer (O\'s) won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('Congrats you won this time!\n** Good Job**!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-------------- New Game ---------------------')
        main()  # call main again 
    else:
        break