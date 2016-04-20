from Cell import Cell


class GetOutOfLoop(Exception):
    pass


class Solver:
    def __init__(self):
        size = 9
        self.sudokuArr = [[0 for x in range(size)] for y in range(size)]
        self.isSolved = False
        self.backUpStack = []
        self.sameNumbers = False
        self.answer = ""

    def doSolve(self, sudoku):
        self.initSudoku(sudoku)
        self.solve()
        if self.isSolved:
            self.printSudoku()
        else:
            self.answer = "999"
        return self.answer

    def initSudoku(self, sudoku):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                cell = Cell(sudoku[i][j])
                cell.setSectorNumber((3 * (i / 3)) + (j / 3))
                self.sudokuArr[i][j] = cell

    def printSudoku(self):
        print("================FINISHED!!===================")
        for i in range(0, 9, 1):
            stringSudoku = ""
            for j in range(0, 9, 1):
                stringSudoku = stringSudoku + str(self.sudokuArr[i][j].integer) + " "
            print(stringSudoku)

    def check(self, line, col, num):
        somethingDone = False

        for i in range(0, 9, 1):
            if (self.sudokuArr[line][i].check(num)):
                somethingDone = True

            if (self.sudokuArr[i][col].check(num)):
                somethingDone = True

            if (num == self.sudokuArr[line][i].getValue()) and (i != col) or (num == self.sudokuArr[i][col].getValue()) \
                    and i != line:
                self.sameNumbers = True

        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if self.sudokuArr[i][j].getSectorNumber() == self.getCurrentSector(line, col):
                    if self.sudokuArr[i][j].check(num):
                        somethingDone = True

                if (num == self.sudokuArr[i][j].getValue()) and (i != line) and (j != col) and \
                        self.sudokuArr[i][j].getSectorNumber() == self.getCurrentSector(line, col):
                    self.sameNumbers = True
        return somethingDone

    def checkForUnique(self, line, col, possibleValues):
        somethingDone = False

        for val in possibleValues:
            isUnique = True
            uniqueNum = val

            for i in range(0, 9, 1):
                if (self.sudokuArr[line][i].contains(uniqueNum)) or (self.sudokuArr[i][col].contains(uniqueNum)):
                    isUnique = False
                    break

            if isUnique:
                try:
                    for i in range(0, 9, 1):
                        for j in range(0, 9, 1):
                            if self.sudokuArr[i][j].contains(uniqueNum) and self.sudokuArr[i][j].getSectorNumber[i][j] == \
                                    self.getCurrentSector(line, col):
                                isUnique = False
                                raise GetOutOfLoop
                except GetOutOfLoop:
                    pass
                if isUnique:
                    self.sudokuArr[line][col].setUnique(uniqueNum)
                    somethingDone = True
        return somethingDone

    def guess(self, numberOfGuesses):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if isinstance(self.sudokuArr[i][j].getValue(), list):
                    valuesList = self.sudokuArr[i][j].getValue()
                    numberOfPossibleGuesses = len(valuesList)
                    if numberOfGuesses == numberOfPossibleGuesses:
                        return False
                    self.sudokuArr[i][j].setUnique(valuesList[numberOfGuesses])
                    return True;
        return False

    def solve(self):
        numberOfGuesses = 0
        self.isSolved = False

        while not self.isSolved:
            self.isSolved = True

            nothingDone = not self.checkValues()

            if self.sameNumbers:
                self.applyBackUp()
                return

            if nothingDone and (not self.isSolved):
                backUp = self.makeBackUp()

                guessed = self.guess(numberOfGuesses)
                if not guessed:
                    self.applyBackUp()
                    return
                else:
                    self.backUpStack.append(backUp)
                    numberOfGuesses += 1
                    self.solve()

    def checkValues(self):
        somethingDone = False
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if (self.sudokuArr[i][j].isFound()) and (not self.sudokuArr[i][j].isChecked()):
                    if self.check(i, j, self.sudokuArr[i][j].getValue()):
                        somethingDone = True
                    self.sudokuArr[i][j].setCheckedTrue()
                elif not self.sudokuArr[i][j].isFound():
                    self.isSolved = False
                    if self.checkForUnique(i, j, self.sudokuArr[i][j].getValue()):
                        somethingDone = True
        return somethingDone

    def makeBackUp(self):
        size = 9
        backUp = [[0 for x in range(size)] for y in range(size)]
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                backUp[i][j] = self.sudokuArr[i][j].clone()
        return backUp

    def applyBackUp(self):
        self.sudokuArr = self.backUpStack.pop()
        self.sameNumbers = False
        self.isSolved = False

    def getCurrentSector(self, line, col):
        return (3 * (line / 3)) + (col / 3)
