from game import Game
from player import  Player
from GameController import GameController
from RNNModel import ConnectFourModelRNN
from NNModel import ConnectFourModelNN
from keras.models import load_model

playerOneVal= -1
playerTwoVal = 1

def main():
    firstGame = Game()
    secondGame = Game()
    thirdGame = Game()
    fourthGame = Game()
    #create players
    print("Creating Players")
    playerOne = Player(playerOneVal, strategy='random')
    playerTwo = Player(playerTwoVal, strategy='random')
    
    playerThree = Player(playerOneVal, strategy='random')
    playerFour = Player(playerTwoVal, strategy='random')
    
    #get training data
    print("Creating Training Data")
    gameControllerNN = GameController(firstGame, playerOne, playerTwo)
    gameControllerNN.simulateManyGames(14500)
    
    gameControllerRNN = GameController(secondGame, playerThree, playerFour)
    gameControllerRNN.simulateManyGames(13000)

    NNmodel = ConnectFourModelNN(42, 3, 50, 100)
    NNmodel.train(gameControllerNN.getTrainingHistory())
    
    RNNmodel = ConnectFourModelRNN(42, 3, 50, 100)
    RNNmodel.train(gameControllerRNN.getTrainingHistory())

    #Create the Deep Q-Learning Agents
    print("Creating Agents")
    playerOneNeural = Player(playerOneVal, strategy='model', model = NNmodel,predicting = True)     
    playerTwoRNN = Player(playerTwoVal, strategy='model', model = RNNmodel, predicting = True)

    #Play the game
    gameControllerFinal = GameController(thirdGame,playerOneNeural,playerTwoRNN)
    print("Playing 500 Games: Deep Q-Learrning with MLP as first player and Deep Q-Learning with RNN as second player")
    gameControllerFinal.simulateManyGames(500)
    
    gameControllerFinal = GameController(fourthGame, playerTwoRNN, playerOneNeural)
    print("Playing 500 Games: Deep Q-Learrning with RNN as first player and Deep Q-Learning with MLP as second player")
    gameControllerFinal.simulateManyGames(500)


