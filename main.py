from game import Game
from player import  Player
from game_controller import GameController
from RNNModel import ConnectFourModelRNN
from model import ConnectFourModel

playerOneVal= -1
playerTwoVal = 1

def main():
    y = []
    x= []
#     i = 14000
    i= 1
    while i <= 100:
        print('value is', i)
        x.append(i)
        firstGame = Game()
        playerOne = Player(playerOneVal, strategy='random')
        playerTwo = Player(playerTwoVal, strategy='random')

        gameController = GameController(firstGame, playerOne, playerTwo)
        print ("Playing with both players with random strategies")
        gameController.simulateManyGames(i)

        RNNmodel = ConnectFourModelRNN(42, 3, 50, 100)
        RNNmodel.train(gameController.getTrainingHistory())
        
        DQNmodel = ConnectFourModel(42, 3, 50, 100)
        DQNmodel.train(gameController.getTrainingHistory())

        playerOneNeural = Player(playerOneVal, strategy='model', model=RNNmodel)         
        playerTwoRNN = Player(playerTwoVal, strategy='model', model=DQNmodel)

        secondGame = Game()
        gameController = GameController(secondGame, playerOneNeural, playerTwoRNN)
        print("Playing with RNN vs DQN")
        res = gameController.simulateManyGames(100)
        y.append(res)
        i += 1

    return x, y


