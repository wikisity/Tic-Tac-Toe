# Author: ARNOLD EPANDA
# Date: 4/5/2016
# E-mail: aepanda1@umbc.edu
# Description: The lines of code below are written in python and designed
# to build the classic game tic-tac-toe. In this game, one player is X and the other player is O.
# Players take turns placing their X or O. If a player gets three of their marks on the board, in
# a row, column, or one of the two diagonals, they win. When the board fills up with neither player
# winning, the game ends in a draw.


import random

# a_char() function returns a letter that is either X or O not both
# Input: The function takes noting as input parameters
# Output: Returns only the symbol X or the symbol O
def a_char():
    a_char= ""
    a_bool = True
    while a_bool: # Continue looping untill the symbol X or the symbol O is generated
        a_char = chr(random.randint(ord("O"), ord("X")))
        if a_char != "O" and a_char != "X":
            a_bool = True
        else:
            a_bool = False

    return a_char


# draw_board() function designs the board that is shown each time a new game starts
# Input: The function has no input
# Ouput: returns a list in which elements are string
def draw_board():
    dash = "-" * 5
    board = ["1", "|", "2", "|", "3", "\n", dash, "\n", "4", "|", "5", "|", "6", "\n", dash, "\n", "7", "|", "8", "|", "9", "\n"]

    return board
    
# update_board() function updates the board that is passed as a parameter
# Input: takes in a list of string. That is, a board
         # then takes in a number or position where a player wants to place his/her symbol. That is, the player choice
         # Lastly, Takes in the symbol to place at the requested choice.
# Ouput: returns the board updated with the symbol of player. The board that is returned is always a list of strings
def update_board(a_board, a_choice, symbol):
    for i in range(len(a_board)):
        if a_board[i] == str(a_choice): # I found player choice/position to insert symbol
            a_board[i] = symbol # I add symbol into player choice
            return a_board
    

# winner() function returns 'True' or 'False' whether a winner is found or not.
# Input: the board and the symbol of player as formal parameters
        # The board is a list of strings and the symbol is either symbol X or symbol O
# Output: Returns "True" if winner is found. Returns "False" if winner is not found
def winner(a_board, symbol):
    SECONDARY_BOARD = 30
    PRIMARY_BOARD = 22
    winnin_in = False
    
    # This is the board that is loaded. It is cast to a type list once loaded.
    if len(a_board) == SECONDARY_BOARD: # Due some some of its elemments its length changes once loaded. Thus, it is called secondary board
        if symbol == "X":
          if a_board[0] == "X" and a_board[2] == "X" and a_board[4] == "X":
                winnin_in = True
            elif a_board[12] == "X" and a_board[14] == "X" and a_board[16] == "X":
                winnin_in = True
            elif a_board[24] == "X" and a_board[26] == "X" and a_board[28] == "X":
                winnin_in = True
            elif a_board[0] == "X" and a_board[12] == "X" and a_board[24] == "X":
                winnin_in = True
            elif a_board[2] == "X" and a_board[14] == "X" and a_board[26] == "X":
                winnin_in = True
            elif a_board[4] == "X" and a_board[16] == "X" and a_board[28] == "X":
                winnin_in = True
            elif a_board[4] == "X" and a_board[14] == "X" and a_board[24] == "X":
                winnin_in = True
            elif a_board[0] == "X" and a_board[14] == "X" and a_board[28] == "X":
                winnin_in = True
        
        elif symbol == "O":
            if a_board[0] == "O" and a_board[2] == "O" and a_board[4] == "O":
                winnin_in = True
            elif a_board[12] == "O" and a_board[14] == "O" and a_board[16] == "O":
                winnin_in = True
            elif a_board[24] == "O" and a_board[26] == "O" and a_board[28] == "O":
                winnin_in = True
            elif a_board[0] == "O" and a_board[12] == "O" and a_board[24] == "O":
                winnin_in = True
            elif a_board[2] == "O" and a_board[14] == "O" and a_board[26] == "O":
                winnin_in = True
            elif a_board[4] == "O" and a_board[16] == "O" and a_board[28] == "O":
                winnin_in = True
            elif a_board[4] == "O" and a_board[14] == "O" and a_board[24] == "O":
                winnin_in = True
            elif a_board[0] == "O" and a_board[14] == "O" and a_board[28] == "O":
                winnin_in = True
  
    # This is the Board that is shown at the start of a new game
    elif len(a_board) == PRIMARY_BOARD:
        if symbol == "X":
            if a_board[0] == "X" and a_board[2] == "X" and a_board[4] == "X":
                winnin_in = True
            elif a_board[8] == "X" and a_board[10] == "X" and a_board[12] == "X":
                winnin_in = True
            elif a_board[16] == "X" and a_board[18] == "X" and a_board[20] == "X":
                winnin_in = True
            elif a_board[0] == "X" and a_board[8] == "X" and a_board[16] == "X":
                winnin_in = True
            elif a_board[2] == "X" and a_board[10] == "X" and a_board[18] == "X":
                winnin_in = True
            elif a_board[4] == "X" and a_board[12] == "X" and a_board[20] == "X":
                winnin_in = True
            elif a_board[4] == "X" and a_board[10] == "X" and a_board[16] == "X":
                winnin_in = True
            elif a_board[0] == "X" and a_board[10] == "X" and a_board[20] == "X":
                winnin_in = True

        elif symbol == "O":
            if a_board[0] == "O" and a_board[2] == "O" and a_board[4] == "O":
                winnin_in = True
            elif a_board[8] == "O" and a_board[10] == "O" and a_board[12] == "O":
                winnin_in = True
            elif a_board[16] == "O" and a_board[18] == "O" and a_board[20] == "O":
                winnin_in = True
            elif a_board[0] == "O" and a_board[8] == "O" and a_board[16] == "O":
                winnin_in = True
            elif a_board[2] == "O" and a_board[10] == "O" and a_board[18] == "O":
                winnin_in = True
            elif a_board[4] == "O" and a_board[12] == "O" and a_board[20] == "O":
                winnin_in = True
            elif a_board[4] == "O" and a_board[10] == "O" and a_board[16] == "O":
                winnin_in = True
            elif a_board[0] == "O" and a_board[10] == "O" and a_board[20] == "O":
                winnin_in = True

    return winnin_in

# error() function returns 'True' or 'False' whether player attempts to fill a space that is already taken
# Input: The board and the position to insert the symbol
# output: returns True if space to insert symbol is alraedy taken. Returns False otherwise
def error(a_board, a_choice):
    error = False
    for k in range(len(a_board)):
        if a_board[k] == str(a_choice): # The equal sign means that this space is not yet taken
            return error

    error = True # The space is likely to have an "O" or a "X". That is, the space is taken
    return error
    

# all_filled() function returns 'True' or 'False' whether all positons are filled or not
# Input: takes in the board only
# Output: returns True if all valid positions are filled already. Returns False if not all positions are filled
def all_filled(a_board):
    count_it = 0
    CONSTANT9 = 9
    all_filled = False
    for i in range(len(a_board)):
        if a_board[i] == "X" or a_board[i] == "O":
            count_it += 1

    if count_it == CONSTANT9:
        all_filled = True
        return all_filled
    else:
        return all_filled

# main() function controls the flow of execution of each instruction of the tic-tac-toe game
def main():
    player1 = 0
    player2 = 0
    symbol_player1 = ""
    symbol_player2 = ""
    SAVE_GAME = -1
    LOAD_GAME = -2
    CONSTANT1 = 1
    CONSTANT2 = 2
    CONSTANT9 = 9
    FIRST_BOARD = 22
    SECOND_BOARD = 30
    FIFTH_LINE_OF_FILE = 5
    LENGTH_LAST_LINE_OF_FILE = 2
    board_filled = False
    found_winner = False
    game_saved = False
    want_to_play = True
    positive_responses = ["Yes", "YeS", "YEs", "YES", "yes", "yeS", "yEs", "yES", "y", "Y"]
    negative_responses = ["no", "nO", "No", "NO", "N", "n"]
  
  print("Welcome to Tic-Tac-Toe")
    print("This is for two players")

    while want_to_play:
        player1 = random.randint(1, 2)
        symbol_player1 = a_char()

        print("Player " + str(player1) + " will go first and will play with the " + symbol_player1)

        this_board = draw_board()
        for element in this_board:
            print(element, end = "") # Display the board at the start of a new game. That is, the primary board
        print()

        board_filled = False
        found_winner = False
        game_saved = False
        while not(found_winner) and not(board_filled) and not(game_saved):
            print("Player " + str(player1) + " what is your choice?")
            player_choice = int(input("(1-9) or " + str(SAVE_GAME) + " to save or " + str(LOAD_GAME) + " to load: "))

            while (player_choice < CONSTANT1 or player_choice > CONSTANT9) and (player_choice != LOAD_GAME and player_choice != SAVE_GAME):
                print("Player " + str(player1) + " what is your choice?")
                player_choice = int(input("(1-9) or " + str(SAVE_GAME) + " to save or " + str(LOAD_GAME) + " to load: "))
            
            if player_choice != SAVE_GAME and player_choice != LOAD_GAME:
                # My first action is to check if the space corresponding to player choice is already taken
                this_error = error(this_board, player_choice)
                while this_error: # If space taken, then continue looping till player chooses another space to insert symbol
                    print("The space is already taken.")
                    print("Player " + str(player1) + " what is your choice?")
                    player_choice = int(input("(1-9) or " + str(SAVE_GAME) + " to save " + str(LOAD_GAME) + " to load: "))
                    
                    while (player_choice < CONSTANT1 or player_choice > CONSTANT9) and (player_choice != LOAD_GAME and player_choice != SAVE_GAME):
                        print("Player " + str(player1) + " what is your choice?")
                        player_choice = int(input("(1-9) or " + str(SAVE_GAME) + " to save or " + str(LOAD_GAME) + " to load: "))
                        
                    this_error = error(this_board, player_choice)

                print()
                # Then my next action is to update the board. In other words, insert symbol into player's choice
                this_board = update_board(this_board, player_choice, symbol_player1)
                # Next, check if there is a winner
                a_winner = winner(this_board, symbol_player1)
                if a_winner:
                    print("Player " + str(player1) + " wins!!!")
                    found_winner = True # Once we find a winner, then we want to start a new game. That is,we change the value of 'found_winner' to 'True'
                else:
                    is_filled = all_filled(this_board) # If winner was not found, then we check if board is filled already
                    if is_filled:
                        board_filled = True
                    else:
                        if not(this_error):
                            # Final step, print the board that is updated and not filled yet
                            for element in this_board:
                                print(element, end = "")
                            print()

                    # We want to switch player and symbol player
                    if player1 == CONSTANT2 and symbol_player1 == "O":
                        player1 = CONSTANT1
                        symbol_player1 = "X"
                    elif player1 == CONSTANT2 and symbol_player1 == "X":
                        player1 = CONSTANT1
                        symbol_player1 = "O"
                    elif player1 == CONSTANT1 and symbol_player1 == "O":
                        player1 = CONSTANT2
                        symbol_player1 = "X"
                    elif player1 == CONSTANT1 and symbol_player1 == "X":
                        player1 = CONSTANT2
                        symbol_player1 = "O"
                        
            # Player choose to load the game
             elif player_choice == LOAD_GAME:
                file_to_load = open("tic.txt")
                my_string1 = file_to_load.readline()
                file_to_load.close()
                if len(my_string1) == 1:
                    print("Error Action Loading. No file was previously saved.")

                elif not(len(my_string1) == 1):
                    this_string2 = ""
                    file_to_load = open("tic.txt")
                    i = 0
                    while i < FIFTH_LINE_OF_FILE:
                        this_string2 += file_to_load.readline()
                        i += 1
                    print("Game Loaded")
                    file_to_load.close()

                    file_to_load = open("tic.txt")
                    this_board = list(this_string2)
                    for line in file_to_load:
                        if len(line.split()) == LENGTH_LAST_LINE_OF_FILE:
                            player1 = int(line.split()[0])
                            symbol_player1 = line.split()[1]

                    file_to_load.close()
                    print(this_string2, end = "")
                    print()

            # Player choose to save the game, then we write into a file
            elif player_choice == SAVE_GAME:
                file_to_save = open("tic.txt", "w")
                dash = "-" * 5
                if len(this_board) == FIRST_BOARD:
                    file_to_save.write(this_board[0] + "|" + this_board[2] + "|" + this_board[4] + "\n" + dash + "\n" + this_board[8] + "|" + this_board[10] + "|" + th\
is_board[12] + "\n" + dash + "\n" + this_board[16] + "|" + this_board[18] + "|" + this_board[20] + "\n" + str(player1) + " " + symbol_player1 + "\n")

                elif len(this_board) == SECOND_BOARD:
                    file_to_save.write(this_board[0] + "|" + this_board[2] + "|" + this_board[4] + "\n" + dash + "\n" + this_board[12] + "|" + this_board[14] + "|" + t\
his_board[16] + "\n" + dash + "\n" + this_board[24] + "|" + this_board[26] + "|" + this_board[28] + "\n" + str(player1) + " " + symbol_player1 + "\n")


                print("File Saved")
                file_to_save.close()
                player_response = input("Play again?: ")
                if player_response in positive_responses:
                    game_saved = True
                # Below, player choose to save the game and does not want to play anymore.
                elif player_response in negative_responses: # In this case I do save player number and its symbol. Then I exit the game
                    print("Thank you for Playing")
                    game_saved = True
                    want_to_play = False

         if (player_choice != LOAD_GAME and player_choice != SAVE_GAME):
            if (board_filled) and (not(found_winner)):
                print("The board is filled and there is no winner.")
                player_response = input("Do you want to play again?: ")
                if player_response in positive_responses:
                    want_to_play = True
                elif player_response in negative_responses:
                    print("Thank you for Playing")
                    want_to_play = False

            elif (found_winner) and (not(board_filled)):
                player_response = input("Do you want to play again?: ")
                if player_response in positive_responses:
                    want_to_play = True
                elif player_response in negative_responses:
                    print("Thank you for playing")
                    want_to_play = False

main()
