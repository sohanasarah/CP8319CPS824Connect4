import os
import copy
import gym
from gym_connect4.envs.connect4_env import Connect4Env

emptyVal = 0
gameStateDraw = 0
gameStateNotEnded = 2
numRows = 6
numCols = 7
requiredSeq = 4


class Game:
    def __init__(self):
        self.resetBoard()

    def resetBoard(self):
        self.game = gym.make('Connect4-v0', height=numRows, width=numCols, connect=4)
        self.board = self.game.board.T[::-1].copy()
        self.board *= 0
        self.boardHistory = []
        self.gameNoStarted = True
    
    def getAvailableMoves(self):
        availableMoves = []
        for j in range(numCols):
            if self.board[numRows - 1][j] == emptyVal:
                availableMoves.append([numRows - 1, j])
            else:
                for i in range(numRows - 1):
                    if self.board[i][j] == emptyVal and self.board[i + 1][j] != emptyVal:
                        availableMoves.append([i, j])
        return availableMoves

    def move(self, col, player):
        zeros = []
        ones = []
        minusones = []
        if self.gameNoStarted:
            self.gameNoStarted=False
        a = self.game.step(col[1])
        self.board = self.game.board.T[::-1].copy()
        self.availableMoves = self.game.get_moves()

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
        pval = 1
        res = 1
        if player.value == -1:
            pval = 0
            res = -1
        res = self.game.get_result(pval)
        self.boardHistory.append(copy.deepcopy(self.board))


    def getBoardHistory(self):
        return self.boardHistory

    def getBoard(self):
        return self.board
    
    def results(self, player):
        return self.game.get_result(player)


