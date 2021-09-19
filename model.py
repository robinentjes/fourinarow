import copy

class Board:

    # this file contains all the information, in regards to the game board
    # the status of the game board is stored as a 2d array, where 0  means that there is no coin,
    # 1 if there is a coin from player 1 and -1 if there is a coin for player 2

    def __init__(self):
        self.__board = [[0 for x in range(7)] for y in range(6)]
        self.__columnFilled = [0 for x in range(7)]
        self.__numberMoves = 0


    def addStone(self, currentPlayer, column):
        self.__numberMoves += 1
        row = 5 - self.__columnFilled[column]
        self.__board[row][column] = currentPlayer
        self.__columnFilled[column] += 1


    def canPlay(self, column):
        return self.__columnFilled[column] < 6


    def isWinningMove(self, currentPlayer, column):
        board2 = copy.deepcopy(self)
        if board2.canPlay(column):
            board2.addStone(currentPlayer, column)
            return board2.isWin(currentPlayer, column)
        return False


    def getBoard(self):
        return self.__board


    def setCellValue(self, x, y, value):
        self.__board[y][x] = value


    # returns true if there is a win
    def isWin(self, currentPlayer, lastColumn, verPos = -1):
        if verPos == -1:
            verPos = 5 - (self.__columnFilled[lastColumn] - 1)
        horPos = lastColumn
        # check horizontal
        chainLen = 0
        for x in range(7):
            if self.__board[verPos][x] == currentPlayer:
                chainLen += 1
                if chainLen >= 4:
                    return True
            else:
                chainLen = 0

        # check vertical
        chainLen = 0
        for y in range(6):
            if self.__board[y][horPos] == currentPlayer:
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

            if self.__board[y][hor] == currentPlayer:
                chainLen += 1
                if chainLen >= 4:
                    return True
            else:
                chainLen = 0
            hor += 1
            if hor > 6:
                break

        # check diagonal from bottom left to top right
        hor = 0
        ver = 5

        if (5 - verPos) > horPos:
            ver = verPos + horPos
        else:
            hor = horPos - (5 - verPos)

        chainLen = 0
        for x in range(hor, 7):
            if self.__board[ver][x] == currentPlayer:
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
        self.__numberMoves = 0


    def getNumberMoves(self):
        return self.__numberMoves


    def printBoard(self):
        for y in range(6):
            for x in range(7):
                if self.__board[y][x] == -1:
                    print(2, end=" ")
                else:
                    print(self.__board[y][x], end=" ")
            print("")
        print("-------------")
        print("1 2 3 4 5 6 7")
