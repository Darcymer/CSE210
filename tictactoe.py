
'''
Author: Darcy Merilan
Stub Code provided by Adam Hayes
'''


def main():
    # assign/get the first player
    player =next_player('')

    nextPlayer = next_player(player)
    print(player)

    # create a board
    board = create_board()
    #create_board()
    
    

    display_board(board)
    print("Thats what we call GG's!!!")

    # loop if there isn't a winner or if the game isn't a draw

        # display the board

        # allow the player to make a move

        # pick the next player

    # display the final board

    # show message for winner and thanks for playing

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    
    board = [ ['0','1','2'],
            ['3','4','5'],
            ['6','7','8']
    ]

    board = list(range(1,10))
    return board


def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print(f'{board[0]}|{board[1]}|{board[2]}|')
    print('--------')
    print(f'{board[3]}|{board[4]}|{board[5]}|')
    print('---------')
    print(f'{board[6]}|{board[7]}|{board[8]}|')
    print()
 

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    for square in range(9):
       if board[square] != 'x' and board[square] != 'o':
           return False
    return True
    

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    '''
    return(board [0] == board[1] == board[2] or
           board [3] == board[4] == board[5] or
           board [6] == board[7] == board[8] or
           board [0] == board[3] == board[6] or
           board [1] == board[4] == board[7] or
           board [2] == board[5] == board[8] or
           board [0] == board[4] == board[8] or
           board [2] == board[4] == board[6])
           '''
    #fix to make it non 2 dimensional
    def check_counts(list):
        ''' return: True if there are 3 x's or o'x in the given list '''
        x_count = list.count('x')
        o_count = list.count('o')
        if (x_count == 3) or (o_count == 3):
            return True
    # check rows
    row = []
    i = 0
    for square in board:
        if i % 3 == 0:
            if check_counts(row):
                return True
            row = []
        row.append(square)
    # check columns
    for i in range(3):
        col = []
        for j in range(0, 9, 3):
            col.append(board[i + j])
        if check_counts(col):
            return True
    # check diagonals
    # diagonal 1
    diagonal = []
    for i in range(0, 9, 4):
        diagonal.append(board[i])
    if check_counts(diagonal):
        return True
    # diagonal 2
    diagonal = []
    for i in range(2, 8, 2):
        diagonal.append(board[i])
    if check_counts(diagonal):
        return True
    # else:
    return False


def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''

    

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == 'x' or current == '':
        return 'o'
    return 'x'
 

# run main if this has been called from the command line
if __name__ == "__main__":
    main()