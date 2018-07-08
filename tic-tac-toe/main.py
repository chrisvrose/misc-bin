#!/usr/bin/env python3

#nyeh


# 0 is unplayed, 1 is O and 2 is X


# set board
def set_board(board, choice , turn):
	position = get_pos(choice)
	print("Checking "+str(position))
	if board[ position[0] ][ position[1] ] == 0 :
		# Set the board to turn
		board[ position[0] ][ position[1] ] = turn
		return True
	else:
		return False



def print_board(board):
	print("\n")
	for i in board:
		print( stringify_turn(i[0]) ," ", stringify_turn(i[1]) ," ", stringify_turn(i[2]) )

	print("\n")


def get_pos(choice):
	# Convert to a number between 0 to 8. This gives a ternary number
	choice-=1
	# Get and flip first index
	a = 2 - choice//3
	# Get second index
	b = choice%3
	return (a,b)


def check_status(board, turn,win_status):
	# Three rows, three columns, two diagonals
	sums = [[0,0,0],[0,0,0],[0,0]]
	# Row sums
	for index, i in enumerate(board):
		for power, j in enumerate(i):
			sums[0][index] += (3**power)*j
			sums[1][power] += (3**index)*j
			sums[2][0] = board[0][0] + 3*board[1][1] + 9*board[2][2]
			sums[2][1] = board[2][0] + 3*board[1][1] + 9*board[0][2]
	sums_collapsed = []
	list.extend(sums_collapsed,sums[0])
	list.extend(sums_collapsed,sums[1])
	list.extend(sums_collapsed,sums[2])
	print(sums_collapsed)
	if 13 in sums_collapsed:
		win_status[0] = 1
		return False
	elif 26 in sums_collapsed:
		win_status[0] = 2
		return False
	else:
		return True

def stringify_player(win_status,choice_p1):
	if win_status==0:
		return "Nobody"
	elif win_status==choice_p1:
		return "Player 1"
	else:
		return "Player 2"



def stringify_turn(turn):
	return " " if turn==0 else ("O" if turn==1 else "X")
	#return "O" if turn==1 else "X"

def intify_choice(choice):
	return 1 if choice=="O" else 2

def main():
	# Init the precious board
	board = [[0,0,0],[0,0,0],[0,0,0]]

	# Ask the player
	choice_p1 = input("Player 1 - O or X?").upper()
	turn = 1 if choice_p1=="O" else 2

	#Holds the status of the game
	win_status = [0]

	# Stays true during gameplay anyways so using that
	while True:
		
		print('\033[H\033[J')
		# Print current board
		print_board(board)
		if check_status(board, turn, win_status):
			choice = int(input("1-9 for input as per numpad, 0 for exit:"))
			# Check if input in the numpad range or u mad
			if choice in range(10):
				# Exit, since user input
				if choice == 0:
					break
				#Check if input was valid
				elif set_board(board , choice , turn):
					print("Valid move, turn "+stringify_player(turn, intify_choice(choice_p1) ))
					turn = 2 if turn == 1 else 1
				#
				else:
					print("There's already something there man, turn "+stringify_player(turn.choice_p1))
			else:
				print("Invalid input, turn"+ stringify_player(turn, intify_choice(choice_p1) ))
		else:
			break
	print(stringify_player(win_status[0], intify_choice(choice_p1) ), win_status[0], intify_choice(choice_p1) )
	print("That's over.")


main()
