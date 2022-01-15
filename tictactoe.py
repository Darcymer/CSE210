
'''
Author: Darcy Merilan
Stub Code provided by Adam Hayes
function for is winner: Daniel Loveless
'''


def main():
    # assign/get the first player
    player =next_player('')

    # create a board
    board = create_board()

    #loop
    while not (is_winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)

    display_board(board)
    print("Thats what we call GG's!!!")


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
    #Displays the current board
    
    print(f'{board[0]}|{board[1]}|{board[2]}|')
    print('------')
    print(f'{board[3]}|{board[4]}|{board[5]}|')
    print('-------')
    print(f'{board[6]}|{board[7]}|{board[8]}|')
    print()
 

def draw(board):
    #this is a loop that allows for wherever the location is, if the game cannot make a winner... its a draw
    # aka if the game cant make any more x's and anymore o's... its a draw
    for location in range(9):
       if board[location] != 'x' and board[location] != 'o':
           return False
    return True
    

def is_winner(board):
    #this code basically allows the winner to be called by these and only these parameters
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

    #group effort in code to look at all possibility for 3 in a row and selesct winner, this is done through a function inside the winner function
    def check_counts(list):
        # return: True if there are 3 x's or o'x in the given list 
        x_count = list.count('x')
        o_count = list.count('o')
        if (x_count == 3) or (o_count == 3):
            return True
    # this checks for 3 in a row for either x or o
    row = []
    i = 0
    for block in board:
        if i % 3 == 0:
            if check_counts(row):
                return True
            row = []
        row.append(block)
          
    # same as above but for columns
    for i in range(3):
        col = []
        for j in range(0, 9, 3):
            col.append(board[i + j])
        if check_counts(col):
            return True
    # same as the previous 2 but for diagonals
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
    #we created a location, asked the player to input a number between 1-9, they selelect it and moves the player
    location = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[location - 1] = player


    

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == 'x' or current == '':
        return 'o'
    return 'x'
 

# run main if this has been called from the command line
if __name__ == "__main__":
    main()