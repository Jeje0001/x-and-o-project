# from IPython.display import clear_output

def display_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[1]} | {board[2]} | {board[3]}")
# test_board = ['#','X','O','X','O','X','O','X','O','X']

# print(display_board(test_board))

def player_input():
    player1=input("What do you want your input to be? X or O").upper()

    while player1 != "X" and player1 != "O":
            player1=input("What do you want your input to be? X or O").upper()


    if player1 == "X":
        player2="O"
    elif player1 == "O":
        player2="X"

    return "Player1 = x"+ player1,"Player2 = "+player2

print(player_input())