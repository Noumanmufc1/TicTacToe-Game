from random import randint
matrix = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]





def main(matrix):
	list1 = []
	printMatrix(matrix)
	tossResult = toss()
	while(True):
		if tossResult:
			tossResult = False
			matrix, list1 = userTurn(matrix, list1)
			printMatrix(matrix)
		else:
			tossResult = True
			matrix, list1 = computerTurn(matrix, list1)
			printMatrix(matrix)
		winOrlose = check(matrix, list1)
		if (winOrlose):
			break
		else:
			continue
	

def printMatrix(matrix):

		  
	print(matrix[0][0] + "|" + matrix[0][1] + "|" + matrix[0][2])
	print("------")
	print(matrix[1][0] + "|" + matrix[1][1] + "|" + matrix[1][2])
	print("------")
	print(matrix[2][0] + "|" + matrix[2][1] + "|" + matrix[2][2])



def toss():
	while(True):
		userChoice = input("Head or Tail: ").lower()
		try:
			if userChoice != "head" and userChoice != "tail":
				raise "Exception"
		except:
			print("Invalid Input. Try Again")
			continue
		else:
			break

	result = randint(1,2)
	if result==1:
		result = "head"
	elif result == 2:
		result = "tail"
	if result == userChoice:
		print("Its your turn")
		return True
	else:
		print("Its computer's turn.")
		return False

def userTurn(matrix, list1):
	
	while(True):
		try:
			userPlace = int(input("Enter the position on which you want to mark: "))
			if (userPlace < 0 or userPlace > 8) or (userPlace in list1):
				raise "Exception"
		except:
			print("Invalid Input. Try again ")
			continue
		else:
			list1.append(userPlace)
			break
	if (userPlace < 3):
		matrix[0][userPlace] = "X"

	elif ( userPlace > 2 and userPlace < 6):
		userPlace = userPlace % 3
		matrix[1][userPlace] = "X"
	else:
		userPlace = userPlace % 3
		matrix[2][userPlace] = "X"

	return matrix, list1




def computerTurn(matrix, list1):
	marked = False

	while (True):

		if ((matrix[0][0] == "O" and matrix[0][1] == "O")):
			if (matrix[0][2] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break
			

		if ( (matrix[0][0] == "O" and matrix[0][2] == "O")):
			if (matrix[0][1] == " "):
				print("The computer has decided to mark in position 1")
				matrix[0][1] = "O"
				list1.append(1)
				marked = True
				break
			

		if ( (matrix[0][2] == "O" and matrix[0][1] == "O")):
			if (matrix[0][0] == " "):
				print("The computer has decided to mark in position 0")
				matrix[0][0] = "O"
				list1.append(0)
				marked = True
				break
			
				

		if ( (matrix[1][0] == "O" and matrix[1][1] == "O")):
			if (matrix[1][2] == " "):
				print("The computer has decided to mark in position 5")
				matrix[1][2] = "O"
				list1.append(5)
				marked = True
				break
			

		if ( (matrix[1][0] == "O" and matrix[1][2] == "O")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break
			

		if ( (matrix[1][1] == "O" and matrix[1][2] == "O")):
			if (matrix[1][0] == " "):
				print("The computer has decided to mark in position 3")
				matrix[1][0] = "O"
				list1.append(3)
				marked = True
				break
			

		if ( (matrix[2][0] == "O" and matrix[2][1] == "O")):
			if (matrix[2][2] == " "):
				print("The computer has decided to mark in position 8")
				list1.append(8)
				matrix[2][2] = "O"
				marked = True
				break
	
		if ( (matrix[2][0] == "O" and matrix[2][2] == "O")):
			if (matrix[2][1] == " "):
				print("The computer has decided to mark in position 7")
				list1.append(7)
				matrix[2][1] = "O"
				marked = True
				break
			

		if ((matrix[2][1] == "O" and matrix[2][2] == "O")):
			if (matrix[2][0] == " "):
				print("The computer has decided to mark in position 6")
				matrix[2][0] = "O"
				list1.append(6)
				marked = True
				break
			

		if ( (matrix[0][0] == "O" and matrix[1][0] == "O")):
			if (matrix[2][0] == " "):
				print("The computer has decided to mark in position 6")
				matrix[2][0] = "O"
				list1.append(3)
				marked = True
				break
			

		if ((matrix[0][0] == "O" and matrix[2][0] == "O")):
			if (matrix[1][0] == " "):
				print("The computer has decided to mark in position 3")
				matrix[1][0] = "O"
				list1.append(3)
				marked = True
				break

		if ( (matrix[2][0] == "O" and matrix[1][0] == "O")):
			if (matrix[0][0] == " "):
				print("The computer has decided to mark in position 0")
				list1.append(0)
				matrix[0][0] = "O"
				marked = True
				break
			
		if ((matrix[0][1] == "O" and matrix[1][1] == "O")):
			if (matrix[2][1] == " "):
				print("The computer has decided to mark in position 7")
				matrix[2][1] = "O"
				list1.append(7)
				marked = True
				break

		if ((matrix[0][1] == "O" and matrix[2][1] == "O")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if ((matrix[1][1] == "O" and matrix[2][1] == "O")):
			if (matrix[0][1] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][1] = "O"
				list1.append(2)
				marked = True
				break

		if ((matrix[0][2] == "O" and matrix[1][2] == "O")):
			if (matrix[2][2] == " "):
				print("The computer has decided to mark in position 8")
				matrix[2][2] = "O"
				list1.append(8)
				marked = True
				break

		if ((matrix[0][2] == "O" and matrix[2][2] == "O")):
			if (matrix[1][2] == " "):
				print("The computer has decided to mark in position 5")
				matrix[1][2] = "O"
				list1.append(5)
				marked = True
				break
			
		if ((matrix[1][2] == "O" and matrix[2][2] == "O")):
			if (matrix[0][2] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break

		if ((matrix[0][0] == "O" and matrix[1][1] == "O")):
			if (matrix[2][2] == " "):
				print("The computer has decided to mark in position 8")
				matrix[2][2] = "O"
				list1.append(8)
				marked = True
				break

		if ((matrix[0][0] == "O" and matrix[2][2] == "O")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if ((matrix[1][1] == "O" and matrix[2][2] == "O")):
			if (matrix[0][0] == " "):
				print("The computer has decided to mark in position 0")
				matrix[0][0] = "O"
				list1.append(0)
				marked = True
				break

		if ((matrix[0][2] == "O" and matrix[1][1] == "O")):
			if (matrix[2][0] == " "):
				print("The computer has decided to mark in position 6")
				matrix[2][0] = "O"
				list1.append(6)
				marked = True
				break
	
		if ((matrix[0][2] == "O" and matrix[2][0] == "O")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break


		if ((matrix[1][1] == "O" and matrix[2][0] == "O")):
			if (matrix[0][2] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break
		if ((matrix[0][0] == "X" and matrix[0][1] == "X")):
			if (matrix[0][2] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break
			

		if ((matrix[0][0] == "X" and matrix[0][2] == "X")):
			if (matrix[0][1] == " "):
				print("The computer has decided to mark in position 1")
				matrix[0][1] = "O"
				list1.append(1)
				marked = True
				break
			

		if ((matrix[0][2] == "X" and matrix[0][1] == "X")):
			if (matrix[0][0] == " "):
				print("The computer has decided to mark in position 0")
				matrix[0][0] = "O"
				list1.append(0)
				marked = True
				break
			
				

		if ((matrix[1][0] == "X" and matrix[1][1] == "X")):
			if (matrix[1][2] == " "):
				print("The computer has decided to mark in position 5")
				matrix[1][2] = "O"
				list1.append(5)
				marked = True
				break
			

		if ((matrix[1][0] == "X" and matrix[1][2] == "X")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break
			

		if ((matrix[1][1] == "X" and matrix[1][2] == "X")):
			if (matrix[1][0] == " "):
				print("The computer has decided to mark in position 3")
				matrix[1][0] = "O"
				list1.append(3)
				marked = True
				break
			

		if ((matrix[2][0] == "X" and matrix[2][1] == "X")):
			if (matrix[2][2] == " "):
				print("The computer has decided to mark in position 8")
				list1.append(8)
				matrix[2][2] = "O"
				marked = True
				break
	
		if ((matrix[2][0] == "X" and matrix[2][2] == "X")):
			if (matrix[2][1] == " "):
				print("The computer has decided to mark in position 7")
				list1.append(7)
				matrix[2][1] = "O"
				marked = True
				break
			

		if ((matrix[2][1] == "X" and matrix[2][2] == "X")):
			if (matrix[2][0] == " "):
				print("The computer has decided to mark in position 6")
				matrix[2][0] = "O"
				list1.append(6)
				marked = True
				break
			

		if ((matrix[0][0] == "X" and matrix[1][0] == "X")):
			if (matrix[2][0] == " "):
				print("The computer has decided to mark in position 6")
				matrix[2][0] = "O"
				list1.append(3)
				marked = True
				break
			

		if ((matrix[0][0] == "X" and matrix[2][0] == "X")):
			if (matrix[1][0] == " "):
				print("The computer has decided to mark in position 3")
				matrix[1][0] = "O"
				list1.append(3)
				marked = True
				break

		if ((matrix[2][0] == "X" and matrix[1][0] == "X")):
			if (matrix[0][0] == " "):
				print("The computer has decided to mark in position 0")
				list1.append(0)
				matrix[0][0] = "O"
				marked = True
				break
			
		if ((matrix[0][1] == "X" and matrix[1][1] == "X")):
			if (matrix[2][1] == " "):
				print("The computer has decided to mark in position 7")
				matrix[2][1] = "O"
				list1.append(7)
				marked = True
				break

		if ((matrix[0][1] == "X" and matrix[2][1] == "X")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if ((matrix[1][1] == "X" and matrix[2][1] == "X")):
			if (matrix[0][1] == " "):
				print("The computer has decided to mark in position 1")
				matrix[0][1] = "O"
				list1.append(1)
				marked = True
				break

		if ((matrix[0][2] == "X" and matrix[1][2] == "X")):
			if (matrix[2][2] == " "):
				print("The computer has decided to mark in position 8")
				matrix[2][2] = "O"
				list1.append(8)
				marked = True
				break

		if ((matrix[0][2] == "X" and matrix[2][2] == "X")):
			if (matrix[1][2] == " "):
				print("The computer has decided to mark in position 5")
				matrix[1][2] = "O"
				list1.append(5)
				marked = True
				break
			
		if ((matrix[1][2] == "X" and matrix[2][2] == "X")):
			if (matrix[0][2] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break

		if ((matrix[0][0] == "X" and matrix[1][1] == "X")):
			if (matrix[2][2] == " "):
				print("The computer has decided to mark in position 8")
				matrix[2][2] = "O"
				list1.append(8)
				marked = True
				break

		if ((matrix[0][0] == "X" and matrix[2][2] == "X")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if ((matrix[1][1] == "X" and matrix[2][2] == "X")):
			if (matrix[0][0] == " "):
				print("The computer has decided to mark in position 0")
				matrix[0][0] = "O"
				list1.append(0)
				marked = True
				break

		if ((matrix[0][2] == "X" and matrix[1][1] == "X")):
			if (matrix[2][0] == " "):
				print("The computer has decided to mark in position 6")
				matrix[2][0] = "O"
				list1.append(6)
				marked = True
				break
	
		if ((matrix[0][2] == "X" and matrix[2][0] == "X")):
			if (matrix[1][1] == " "):
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break


		if ((matrix[1][1] == "X" and matrix[2][0] == "X")):
			if (matrix[0][2] == " "):
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break

		if (matrix[0][0] == "X" and matrix[0][2] == "X" and matrix[0][1] == "O"):
			if matrix[1][1] == " ":
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if (matrix[0][0] == "X" and matrix[2][0] == "X" and matrix[1][0] == "O"):
			if matrix[1][1] == " ":
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if (matrix[0][2] == "X" and matrix[2][2] == "X" and matrix[1][2] == "O"):
			if matrix[1][1] == " ":
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if (matrix[2][0] == "X" and matrix[2][2] == "X" and matrix[2][1] == "O"):
			if matrix[1][1] == " ":
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break

		if (matrix[0][0] == "X" and matrix[2][2] == "X" and matrix[1][1] == "O"):
			if matrix[0][1] == " ":
				print("The computer has decided to mark in position 1")
				matrix[0][1] = "O"
				list1.append(1)
				marked = True
				break
			if matrix[1][0] == " ":
				print("The computer has decided to mark in position 3")
				matrix[1][0] = "O"
				list1.append(3)
				marked = True
				break
			if matrix[1][2] == " ":
				print("The computer has decided to mark in position 5")
				matrix[1][2] = "O"
				list1.append(5)
				marked = True
				break
			if matrix[2][1] == " ":
				print("The computer has decided to mark in position 7")
				matrix[2][1] = "O"
				list1.append(7)
				marked = True
				break

		if (matrix[0][2] == "X" and matrix[2][0] == "X" and matrix[1][1] == "O"):
			if matrix[0][1] == " ":
				print("The computer has decided to mark in position 1")
				matrix[0][1] = "O"
				list1.append(1)
				marked = True
				break
			if matrix[1][0] == " ":
				print("The computer has decided to mark in position 3")
				matrix[1][0] = "O"
				list1.append(3)
				marked = True
				break
			if matrix[1][2] == " ":
				print("The computer has decided to mark in position 5")
				matrix[1][2] = "O"
				list1.append(5)
				marked = True
				break
			if matrix[2][1] == " ":
				print("The computer has decided to mark in position 7")
				matrix[2][1] = "O"
				list1.append(7)
				marked = True
				break

		if (matrix[1][2] == "X" and matrix[2][1] == "X"):
			if matrix[0][2] == " ":
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break

		if (matrix[1][0] == "X" and matrix[2][1] == "X"):
			if matrix[0][2] == " ":
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break

		if matrix[1][2] == "X" and matrix[2][0] == "X":
			if matrix[0][2] == " ":
				print("The computer has decided to mark in position 2")
				matrix[0][2] = "O"
				list1.append(2)
				marked = True
				break


		if matrix[0][0] == "X" or matrix[2][0] == "X" or matrix[0][2] == "X" or matrix[2][0] == "X":
			if matrix[1][1] == " ":
				print("The computer has decided to mark in position 4")
				matrix[1][1] = "O"
				list1.append(4)
				marked = True
				break
			
		

		if matrix[0][0] == " ":
			print("The computer has decided to mark in position 0. ")
			matrix[0][0] = "O"
			list1.append(0)
			marked = True
			break

		if matrix[2][2] == " ":
			print("The computer has decided to mark in position 8")
			matrix[2][2] = "O"
			list1.append(8)
			marked = True
			break

		if matrix[0][2] == " ":
			print("The computer has decided to mark in position 2")
			matrix[0][2] = "O"
			list1.append(2)
			marked = True
			break

		if matrix[2][0] == " ":
			print("The computer has decided to mark in position 6")
			matrix[2][0] = "O"
			list1.append(6)
			marked = True
			break

		if matrix[1][1] == " ":
			print("The computer has decided to mark in position 4")
			matrix[1][1] = "O"
			list1.append(4)
			marked = True
			break
	

		if not(marked):
			while(True):
				try:
					computerPlace = randint(0,8)
					if (computerPlace in list1):
						raise "Exception"
				except:
					continue
				else:
					list1.append(computerPlace)
					print("The computer has decided to mark on position ", computerPlace)
					if (computerPlace < 3):
						matrix[0][computerPlace] = "O"

					elif ( computerPlace > 2 and computerPlace < 6):
						computerPlace = computerPlace % 3
						matrix[1][computerPlace] = "O"
					else:
						computerPlace = computerPlace % 3
						matrix[2][computerPlace] = "O"
					break
			break
	
		
	return matrix, list1


def check(matrix, list1):
	if ((matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X") or (matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X") or (matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X") or (matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X") or (matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X") or (matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X") or (matrix[0][0] == "X" and matrix[1][1] == "X" and  matrix[2][2] == "X") or (matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X")):
		print("Congratulations. You have won. ")
		return True
	elif ((matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O") or (matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O") or (matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O") or (matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O") or (matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O") or (matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O") or (matrix[0][0] == "O" and matrix[1][1] == "O" and  matrix[2][2] == "O") or (matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O")):
		print("Sorry. The computer has won. ")
		return True
	elif (0 in list1 and 1 in list1 and 2 in list1 and 3 in list1 and 4 in list1 and 5 in list1 and 6 in list1 and 7 in list1 and 8 in list1):
		print("It's a draw.")
		return True
	else:
		return False

main(matrix)


