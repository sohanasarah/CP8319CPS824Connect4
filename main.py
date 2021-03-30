from game import Game
from player import  Player
from game_controller import GameController
from RNNModel import ConnectFourModelRNN


playerOneVal= -1
playerTwoVal = 1

def main():
    y = []
    x=[]
    i = 14000
    while i <= 14000:
        print(i)
        x.append(i)
        firstGame = Game()
        playerOne = Player(playerOneVal, strategy='random')
        playerTwo = Player(playerTwoVal, strategy='random')

        gameController = GameController(firstGame, playerOne, playerTwo)
        print ("Playing with both players with random strategies")
        gameController.simulateManyGames(i)

        model = ConnectFourModelRNN(42, 3, 50, 100)
        model.train(gameController.getTrainingHistory())

        playerOneNeural = Player(playerOneVal, strategy='model', model=model)
#         playerTwoNeural = Player(playerTwoVal, strategy='model', model=model)

        secondGame = Game()
        gameController = GameController(secondGame, playerOneNeural, playerTwo)
        print("Playing with player 1 as Neural Network")
        res = gameController.simulateManyGames(100)
        y.append(res)
        i+= 500

        break

    return x, y


