# CP8319CPS824Connect4

## **The game of Connect4 with Deep Q-Learning**

Evaluation.ipynb runs the project and shows the game results.
The project contains the following classes-

  The ***Game*** Class (game.py)- contains the board of the game, the board history, the game states, the available moves and the results.
  
  The ***Player*** Class(player.py)- it has two strategies- first one is a random strategy, where the player randomly chooses a move from the list of available moves.
  The second one is based on the Neural Network model (MultiLayer Perceptron or Recurrent Neural Network) 
  
  The ***Game Controller*** Class (gameController.py)- it controls the flow of the games. it simulates multiple games and collects the board history from the Game class 
  and build a training history. It takes the available moves from the board and let the player choose the move. Then it passes that move back to the board.
  At the end of the game, it takes the board history and the winner of that game and add them to the training history.
  
  The ***NN Model*** Class (nnModel.py)- contains the model for Multilayer Perceptron. To train the model we take data from the Game Controller and pass it through this model. 
  It also has a predict method which returns the predicted outcome of the model.
  
  The ***RNN Model*** Class (rnnModel.py)- same as NN model but contains the model for Recurrent Neural Network.
  
  The ***Main*** Class(main.py)- this class creates instances of the game and creates the players. Then it trains the players with the desired models and makes them play the game.
  
  
