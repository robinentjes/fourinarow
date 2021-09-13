

class Board:

    # 6x7 playfield
    # 0 means no stone in field, 1 is for player one, and 2 is for player two
    def __init__(self):
        self.__board = [[0 for x in range(7)] for y in range(6)]
        self.__columnFilled = [0 for x in range(7)]

    # updates the board, returns true if it was successful
    # its not successful when board is already full
    def addStone(self, columnNr, playerNr):
        if (self.__columnFilled[columnNr] >= 6):
            return False

        row = 5 - self.__columnFilled[columnNr]
        self.__board[row][columnNr] = playerNr
        self.__columnFilled[columnNr] += 1
        return True


    def getBoard(self):
        return self.__board

    # returns if there is a win
    def isWin(self, playerNr, lastColumn):
        verPos = 5 - (self.__columnFilled[lastColumn] - 1)
        horPos = lastColumn
        # check horizontal
        chainLen = 0
        for x in range(7):
            if self.__board[verPos][x] == playerNr:
                chainLen += 1
                if chainLen >= 4:
                    return True
            else:
                chainLen = 0

        # check vertical
        chainLen = 0
        for y in range(6):
            if self.__board[y][horPos] == playerNr:
                chainLen += 1
                if chainLen >= 4:
                    return True
            else:
                chainLen = 0

        # check diagonal from top left to bottom right
        hor = 0
        ver = 0
        if verPos > horPos:
            ver = verPos - horPos
        else:
            hor = horPos - verPos

        chainLen = 0
        for y in range(ver, 6):

            if self.__board[y][hor] == playerNr:
                chainLen += 1
                if chainLen >= 4:
                    return True
            else:
                chainLen = 0
            hor += 1
            if hor > 6:
                break

        hor = 0
        ver = 5

        if (5 - verPos) > horPos:
            ver = verPos + horPos
        else:
            hor = horPos - (5 - verPos)

        chainLen = 0
        for x in range(hor, 7):
            if self.__board[ver][x] == playerNr:
                chainLen += 1
                if chainLen >= 4:
                    return True
            else:
                chainLen = 0
            ver -= 1
            if ver < 0:
                break
        return False

    def clearBoard(self):
        self.__board = [[0 for x in range(7)] for y in range(6)]
        self.__columnFilled = [0 for x in range(7)]

    def printBoard(self):
        for y in range(6):
            for x in range(7):
                print(self.__board[y][x], end=" ")
            print("")
        print("-------------")
        print("1 2 3 4 5 6 7")
