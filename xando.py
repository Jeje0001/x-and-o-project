# from IPython.display import clear_output

def display_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[1]} | {board[2]} | {board[3]}")
# test_board = ['#','X','O','X','O','X','O','X','O','']
test= [str(i) for i in range(10)]

print(display_board(test))

def player_input():
    player1=input("What do you want your input to be? X or O").upper()

    while player1 != "X" and player1 != "O":
            player1=input("What do you want your input to be? X or O").upper()


    if player1 == "X":
        player2="O"
    elif player1 == "O":
        player2="X"

    return "Player1 = x"+ player1,"Player2 = "+player2

# print(player_input())

def place_marker(board,marker,position):
    if position < 1 or position > 9:
        print("Error value must be between 1 and 9 (inclusive)")
    board[position]=marker
    return board

board = [" "] * 10
# print(place_marker(board, "X", 8))

def wincheck(board,mark):
    winning=[
        (1,2,3),
        (1,4,7),
        (1,5,9),
        (4,5,6),
        (7,5,3),
        (2,5,8),
        (3,6,9),
        (7,8,9),
        (3,5,7)
    ]
    for winnings in winning:
        if board[winnings[0]] == board[winnings[1]] == board[winnings[2]] == mark:
            return True
    return False


# print(wincheck(test_board,'O'))

import random

def first():
    x=random.randint(0,1)
    if x == 0:
        return "Player 1"
    elif x == 1:
        return "Player 2"
    
# first()


def space_check(board, position):
    if board[position] == "":
        return True
    return False

# print(space_check(test_board,9))


def full_board_check(board):
    for a in board:
        if a == "":
            return True
        
    return False
    

# print(full_board_check(test_board))

def player_choice(board):
    free=int(input("What position on the board do you want"))
    x=space_check(board,free)

    if x == True:
        return True
    else:
        return False


# print(player_choice(test_board))


def replay():
    ans=input("Do you want to play again enter Y or N").upper()

    if ans == "Y":
        return True
    else:
        return False


def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    while True:
        board=[""] * 10


        player1_m,player2_m=player_input()

        turn=first()
        print(turn)
        print(f"{turn} will go first")
        play_game = input("Are you ready to play? Enter Y or N: ").upper()
        if play_game != "Y":
            break
        game_on=True

        while game_on:
            if turn == "Player 1":
                display_board(board)
                try:
                    position=int(input("Player 1, Choose your position(1-9):"))
                except ValueError:
                    position=int(input("Player 1, Choose your position(1-9):"))



                if space_check(board,position):
                    place_marker(board,player1_m[-1],position)

                    if wincheck(board,player1_m[-1]):
                        display_board(board)
                        print("Congratulations! player 1 has won the game")
                        game_on=False
                    else:
                        if not full_board_check(board):
                            display_board(board)
                            print("This game is a draw")
                        else:
                            turn="Player 2"
                else:
                    print("That position is not available. Please try another position")
            else:
                display_board(board)
                try:
                    position=int(input("Player 2, Choose your position(1-9)"))
                except ValueError:
                    position=int(input("Player 2, Choose your position(1-9)"))




                if space_check(board,position):
                    place_marker(board,player2_m[-1],position)

                    if wincheck(board,player2_m[-1]):
                        display_board(board)
                        print("Congratulations! Player 2 has won the game")
                        game_on=False
                    else:
                        if not full_board_check(board):
                            display_board(board)
                            print("This game is a draw")
                        else:
                            turn="Player 1"
                else:
                    print("That position is not available. Please try another position")
        if not replay():
            print("Thanks for playing")
            break


            
tic_tac_toe()