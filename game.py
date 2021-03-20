import os
import copy
import gym
from gym_connect4.envs.connect4_env import Connect4Env



RED_PLAYER = 'R'
YELLOW_PLAYER = 'Y'
RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
EMPTY = ' '
EMPTY_VAL = 0
HORIZONTAL_SEPARATOR = ' | '
GAME_STATE_X = -1
GAME_STATE_O = 1
GAME_STATE_DRAW = 0
GAME_STATE_NOT_ENDED = 2
VERTICAL_SEPARATOR = '__'
NUM_ROWS = 6
NUM_COLUMNS = 7
REQUIRED_SEQUENCE = 4


class Game:

    def __init__(self):
        
        self.resetBoard()

    def resetBoard(self):
        self.game = gym.make('Connect4-v0', height=NUM_ROWS, width=NUM_COLUMNS, connect=2)
        self.board = self.game.board.T[::-1].copy()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i,j] = 0
#         self.availableMoves = self.game.get_moves()
        self.boardHistory = []
        self.gameNoStarted = True

    def printBoard(self):
        return    
#     print(self.board)
    
    def getAvailableMoves(self):
        availableMoves = []
        for j in range(NUM_COLUMNS):
            if self.board[NUM_ROWS - 1][j] == EMPTY_VAL:
                availableMoves.append([NUM_ROWS - 1, j])
            else:
                for i in range(NUM_ROWS - 1):
                    if self.board[i][j] == EMPTY_VAL and self.board[i + 1][j] != EMPTY_VAL:
                        availableMoves.append([i, j])
        return availableMoves

#         return self.game.get_moves()

    def getGameResult(self):
        if self.gameNoStarted:
            return 2
        winnerFound = False
        currentWinner = None
        
        # Find winner on horizontal
        for i in range(NUM_ROWS):
            if not winnerFound:
                for j in range(NUM_COLUMNS - REQUIRED_SEQUENCE - 1):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j + 2] and \
                            self.board[i][j] == self.board[i][j + 3]:
                        currentWinner = self.board[i][j]
                        winnerFound = True

        # Find winner on vertical
        if not winnerFound:
            for j in range(NUM_COLUMNS):
                if not winnerFound:
                    for i in range(NUM_ROWS - REQUIRED_SEQUENCE - 1):
                        if self.board[i][j] != 0 and self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i+2][j] and \
                                self.board[i][j] == self.board[i+3][j]:
                            currentWinner = self.board[i][j]
                            winnerFound = True

        # Check lower left diagonals
        if not winnerFound:
            for i in range(NUM_ROWS - REQUIRED_SEQUENCE - 1):
               j = 0
               while j <= i:
                   if self.board[i][j] != 0 and self.board[i][i] == self.board[i + 1][j + 1] and self.board[i][i] == self.board[i + 2][j + 2] and \
                           self.board[i][i] == self.board[i + 3][j + 3]:
                       currentWinner = self.board[i][j]
                       winnerFound = True
                   j = j+1

        # Check upper right diagonals
        if not winnerFound:
            for j in range(NUM_COLUMNS - REQUIRED_SEQUENCE - 1):
                i = j
                while i<= NUM_ROWS - REQUIRED_SEQUENCE - 1:
                    if self.board[i][j] != 0 and self.board[i][i] == self.board[i + 1][j + 1] and self.board[i][i] == self.board[i + 2][j + 2] and \
                            self.board[i][i] == self.board[i + 3][j + 3]:
                        currentWinner = self.board[i][j]
                        winnerFound = True
                    i = i+1

        if winnerFound: return currentWinner
        else:
            drawFound = True
            # Check for draw
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == EMPTY_VAL:
                        drawFound = False
            if drawFound:
                return GAME_STATE_DRAW
            else:
                return GAME_STATE_NOT_ENDED

    def move(self, col, player):
        if self.gameNoStarted:
            self.gameNoStarted=False
        a = self.game.step(col[1])
        self.board = self.game.board.T[::-1].copy()
        self.availableMoves = self.game.get_moves()
        zeros = []
        ones = []
        minusones = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    zeros.append([i,j])
                elif self.board[i][j] == 1:
                    ones.append([i,j])
                else:
                    minusones.append([i,j])

        for elem in zeros:
            self.board[elem[0]][elem[1]] = -1
        for elem in ones:
            self.board[elem[0]][elem[1]] = 1
        for elem in minusones:
            self.board[elem[0]][elem[1]] = 0
        
    
        self.boardHistory.append(copy.deepcopy(self.board))


    def getBoardHistory(self):
        return self.boardHistory

    def getBoard(self):
        return self.board


