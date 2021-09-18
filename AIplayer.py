from model import Board
import copy
import random

def negaMax(board, currentPlayer, alpha, beta, depth):
    if depth == 0:
        return heuristicScore(board, currentPlayer)

    if board.getNumberMoves() == 42:
        return 0

    for x in range(7):
        if board.canPlay(x) and board.isWinningMove(currentPlayer, x):
            return 43 - board.getNumberMoves() / 2

    max = 41 - board.getNumberMoves() / 2
    if beta > max:
        beta = max
        if alpha >= beta:
            return beta

    for x in range(7):
        board2 = copy.deepcopy(board)
        if board2.canPlay(x):
            board2.addStone(currentPlayer, x)

            score = -negaMax(board2, -currentPlayer, -beta, -alpha, depth - 1)
            score += columnBonus(x)
            if score >= beta:
                return score
            if score > alpha:
                alpha = score
    return alpha

def decideMove(board):
    max = -50
    maxX = -1
    for x in range(7):
        if board.canPlay(x):
            board2 = copy.deepcopy(board)
            board2.addStone(-1, x)
            score = - negaMax(board2, 1, -21, 21, 4)
            if score > max:
                max = score
                maxX = x
    return maxX

# we want to determine the number of open three in a rows, a certain amount of points is given for possible wins
def heuristicScore(board, currentPlayer):
    score = 0
    for y in range(6):
        for x in range(7):
            if (board.getBoard())[y][x] == 0:
                board2 = copy.deepcopy(board)
                board2.setCellValue(x, y, currentPlayer)
                if board2.isWin(currentPlayer, x, y):
                    score += 2
    return score

def columnBonus(column):
    columnBaseScores = [0, 0.025, 0.05, 0.1, 0.05, 0.025, 0]
    return columnBaseScores[column] * random.random()
