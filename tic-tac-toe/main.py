#nyeh
def set_board(board, choice):
	return False


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
