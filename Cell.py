import copy


class Cell:
    def __init__(self, integer):
        self.sectorNumber = 0
        if integer != 0:
            self.integer = integer
            self.foundInt = True
            self.checkedInt = False
        else:
            self.possibleValues = []
            for i in range(1, 10, 1):
                self.possibleValues.append(i)
                self.integer = 0
                self.foundInt = False
                self.checkedInt = False

    def setSectorNumber(self, sectorNumber):
        self.sectorNumber = sectorNumber

    def getSectorNumber(self):
        return self.sectorNumber

    def isFound(self):
        return self.foundInt

    def isChecked(self):
        return self.checkedInt

    def setCheckedTrue(self):
        self.checkedInt = True

    def check(self, num):
        if not self.foundInt:
            if not self.possibleValues.__contains__(num):
                return False
            self.possibleValues.remove(num)
            if len(self.possibleValues) == 1:
                self.integer = self.possibleValues[0]
                self.foundInt = True
        return True

    def getValue(self):
        if self.foundInt:
            return self.integer
        else:
            return self.possibleValues

    def contains(self, num):
        return False if self.foundInt else num in self.possibleValues

    def setUnique(self, num):
        self.foundInt = True
        self.integer = num

    def clone(self):
        return copy.deepcopy(self)
