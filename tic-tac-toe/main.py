#nyeh


# set board
def set_board(board, choice):
	position = get_pos(choice)
	print("Checking "+str(position))
	if board[position[0]][position[1]] == 0 :
		return True
	else:
		return False



def print_board(board):
	print("boo")


def get_pos(choice):
	# Convert to a number between 0 to 8. This gives a ternary number
	choice-=1
	# Get and flip first index
	a = 2 - choice//3
	# Get second index
	b = choice%3
	return (a,b)

def main():
	board = [[0,0,0],[0,0,0],[0,0,0]]
	turn = 1
	while True:
		choice = int(input("1-9 for input as per numpad, 0 for exit:"))
		# Check if input in the numpad range or u mad
		if choice in range(10):
			# Exit, since user input
			if choice == 0:
				break
			#Check if input was valid
			elif set_board(board,choice):
				print("Valid move, turn "+str(turn))
				turn = 2 if turn == 1 else 1
			#
			else:
				print("There's already something there man")
		else:
			print("Invalid input")
	print("hi")


main()
