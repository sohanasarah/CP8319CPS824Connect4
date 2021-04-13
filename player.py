import random
import copy
import numpy as np

playerOne = -1

class Player:
    def __init__(self, value, strategy='random', model=None, predicting = False):
        self.value = value
        self.strategy = strategy
        self.model = model
        self.predicting = predicting

    def getMove(self, availableMoves, board):
        if self.strategy == "random":
            return availableMoves[random.randrange(0, len(availableMoves))]
        else:
            maxValue = 0
            bestMove = availableMoves[0]
            values = []
            for availableMove in availableMoves:  
                boardCopy = copy.deepcopy(board)
                boardCopy[availableMove[0]][availableMove[1]] = self.value
                if self.value == playerOne:
                    value = self.model.predict(boardCopy, 2)
                    values.append(value)
                else:
                    value = self.model.predict(boardCopy, 0)
                    values.append(value)        
                if value > maxValue:
                    maxValue = value
                    bestMove = availableMove
            if self.predicting:
                values = np.array(values)
                valuesProb = np.exp(values) / (sum(np.exp(values)))
                dic = {}
                val = random.sample(list(valuesProb), 1)[0]
                c = 0
                for i in range(0, 1):
                    val = random.sample(list(valuesProb), 1)[0]
                    if val in dic:
                        dic[val] += 1
                    else:
                        dic[val] = 1
                for key in dic:
                    if dic[key] > c:
                        val = key
                
                for i in range(len(values)):
                    if valuesProb[i] == val:
                        bestMove = availableMoves[i]
                        break
            return bestMove

    def getPlayer(self):
        return self.value