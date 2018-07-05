#nyeh
def set_board(board, choice):
	print(get_pos(choice))
	return True


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
	while True:
		choice = int(input("1-9 for input as per numpad, 0 for exit:"))
		# Check if input in the numpad range or u mad
		if choice in range(10):
			# Exit, since user input
			if choice == 0:
				break
			#Check if input was valid
			elif set_board(board,choice):
				print("stuff")
			#
			else:
				print("There's already something there man")
		else:
			print("Invalid input")
	print("hi")


main()
