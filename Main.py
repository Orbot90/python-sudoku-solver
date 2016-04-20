#!/usr/bin/python

from Solver import Solver


def readSudokuFromFile(fileName):
    with open("./sudoku.txt") as sudokuFile:
        content = sudokuFile.readlines()
    sudoku = []
    for i in range(0, 9, 1):
        line = content[i].strip().split(' ')
        for j in range(0, 9, 1):
            line[j] = int(line[j])
        sudoku.append(line)
    return sudoku


sudoku = readSudokuFromFile("./sudoku.txt")
solver = Solver()
solver.doSolve(sudoku)

