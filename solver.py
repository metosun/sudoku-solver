import numpy as np
import sys
f = open('sudoku.txt', 'r')

line = f.readline()
sudoku = []
while line:
	line = line.split('\n')[0]
	arr = line.split(',')
	arr = [int(i) for i in arr]
	line = f.readline()
	sudoku.append(arr)
	
def solver(y,x,p):
	for i in range(0,9):
		if sudoku[i][x] == p:
			return False
	for i in range(0,9):
		if sudoku[y][i] == p:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3

	for i in range(0,3):
		for j in range(0,3):
			if sudoku[y0+i][x0+j] == p:
				return False
	return True

def solution():
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0:
				for p in range(1,10):
					if solver(y,x,p):
						sudoku[y][x] = p	
						solution()
						sudoku[y][x] = 0
				return
	print(np.matrix(sudoku))
	sys.exit()

print(np.matrix(sudoku))
solution()
