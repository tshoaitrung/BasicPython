### Print big: print a letter by the dot with a letter by 5*4 or 5*5 matrix
### for example:
"""letter a will persented by
	 **
	*  *
	*  *
	****
	*  *
   letter b will persented by
	***
	*  *
	***
	*  *
	***
"""
def print_by_dot(matrix_letter):
	for row in matrix_letter:
		tmp = "\t"
		for col in row:
			if col == 0:
				tmp = tmp + ' '
			else:
				tmp = tmp + '*'
		print(tmp)


def letter_dot(letter):
	if letter == 'a' or letter == 'A':
		return [[0,1,1,0], [1,0,0,1], [1,0,0,1], [1,1,1,1], [1,0,0,1]]
	if letter == 'b' or letter == 'B':	
		return [[1,1,1,0], [1,0,0,1], [1,1,1,0], [1,0,0,1], [1,1,1,0]]
	if letter == 'c' or letter == 'C':
		return [[0,1,1,1], [1,0,0,0], [1,0,0,0], [1,0,0,0], [0,1,1,1]]
	if letter == 'd' or letter == 'D':
		return [[1,1,1,0], [1,0,0,1], [1,0,0,1], [1,0,0,1], [1,1,1,0]]
	if letter == 'e' or letter == 'E':
		return [[1,1,1,1], [1,0,0,0], [1,1,1,0], [1,0,0,0], [1,1,1,1]]
	if letter == 'f' or letter == 'F':
		return [[1,1,1,1], [1,0,0,0], [1,1,1,0], [1,0,0,0], [1,0,0,0]]
	if letter == 'g' or letter == 'G':
		return [[0,1,1,1], [1,0,0,0], [1,0,1,1], [1,0,0,1], [0,1,1,1]]
	if letter == 'h' or letter == 'H':
		return [[1,0,0,1], [1,0,0,1], [1,1,1,1], [1,0,0,1], [1,0,0,1]]
	if letter == 'i' or letter == 'I':
		return [[1,1,1,0], [0,1,0,0], [0,1,0,0], [0,1,0,0], [1,1,1,0]]
	if letter == 'j' or letter == 'J':
		return [[1,1,1,1], [0,0,0,1], [0,0,0,1], [1,0,0,1], [0,1,1,0]]
	if letter == 'k' or letter == 'K':
		return [[1,0,0,1], [1,0,1,0], [1,1,0,0], [1,0,1,0], [1,0,0,1]]
	if letter == 'l' or letter == 'L':
		return [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,1], [1,1,1,1]]
	if letter == 'm' or letter == 'M':
		return [[1,0,0,0,1], [1,1,0,1,1], [1,0,1,0,1], [1,0,0,0,1], [1,0,0,0,1]]
	if letter == 'n' or letter == 'N':
		return [[1,0,0,0,1], [1,1,0,0,1], [1,0,1,0,1], [1,0,0,1,1], [1,0,0,0,1]]
	if letter == '0' or letter == 'O':
		return [[0,1,1,0], [1,0,0,1], [1,0,0,1], [1,0,0,1], [0,1,1,0]]
	if letter == 'p' or letter == 'P':	
		return [[1,1,1,0], [1,0,0,1], [1,0,0,1], [1,1,1,0], [1,0,0,0]]
	if letter == 'q' or letter == 'Q':
		return [[0,1,1,0], [1,0,0,1], [1,0,0,1], [1,0,1,1], [0,1,1,1]]
	if letter == 'r' or letter == 'R':	
		return [[1,1,1,0], [1,0,0,1], [1,0,0,1], [1,1,1,0], [1,0,0,1]]
	if letter == 's' or letter == 'S':
		return [[1,1,1,1], [1,0,0,0], [0,1,1,0], [0,0,0,1], [1,1,1,1]]
	if letter == 't' or letter == 'T':
		return [[1,1,1,1,1], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,0,0,0]]
	if letter == 'u' or letter == 'U':
		return [[1,0,0,1], [1,0,0,1], [1,0,0,1], [1,0,0,1], [0,1,1,0]]
	if letter == 'v' or letter == 'V':
		return [[1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [0,0,1,0,0]]
	if letter == 'w' or letter == 'W':
		return [[1,0,1,0,1], [1,0,1,0,1], [1,0,1,0,1], [1,0,1,0,1], [0,1,0,1,0]]
	if letter == 'x' or letter == 'X':
		return [[1,0,0,0,1], [0,1,0,1,0], [0,0,1,0,0], [0,1,0,1,0], [1,0,0,0,1]]
	if letter == 'y' or letter == 'Y':
		return [[1,0,0,0,1], [0,1,0,1,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0]]
	if letter == 'z' or letter == 'Z':
		return [[1,1,1,1,1], [0,0,0,1,0], [0,0,1,0,0], [0,1,0,0,0], [1,1,1,1,1]]
	return ""

INPUT = input('Insert the letter you want from A to Z: ')
print('The result will be: \n')
print_by_dot(letter_dot(INPUT))
