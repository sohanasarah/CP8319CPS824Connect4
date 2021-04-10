from game import Game
from player import  Player
from game_controller import GameController
from RNNModel import ConnectFourModelRNN
from model import ConnectFourModel
from keras.models import load_model

playerOneVal= -1
playerTwoVal = 1

def main():
  
    firstGame = Game()
    secondGame = Game()
    
    playerOne = Player(playerOneVal, strategy='random')
    playerTwo = Player(playerTwoVal, strategy='random')
    playerThree = Player(playerOneVal, strategy='random')
    playerfOUR = Player(playerTwoVal, strategy='random')

    gameControllerNN = GameController(firstGame, playerOne, playerTwo)
    gameControllerNN.simulateManyGames(14500)
    
    gameControllerRNN = GameController(secondGame, playerThree, playerfOUR)
    gameControllerRNN.simulateManyGames(13000)

    NNmodel = ConnectFourModel(42, 3, 50, 100)
    NNmodel.train(gameControllerNN.getTrainingHistory())

    RNNmodel = ConnectFourModelRNN(42, 3, 50, 100)
    RNNmodel.train(gameControllerRNN.getTrainingHistory())


    playerOneNeural = Player(playerOneVal, strategy='model', model = RNNmodel)         
    playerTwoRNN = Player(playerTwoVal, strategy='model', model = NNmodel)

    
    thirdGame = Game()
    gameControllerFinal = GameController(thirdGame, playerOneNeural, playerTwoRNN)
    print("Playing with NN as player 1")
    res = gameControllerFinal.simulateManyGames(100)


