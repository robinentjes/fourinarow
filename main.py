from model import Board
from controller import Controller
from view import View

if __name__ == "__main__":
    board = Board()
    c = Controller(board)
    c.mainMenuControl()
