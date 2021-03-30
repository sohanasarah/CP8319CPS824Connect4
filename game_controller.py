import copy

class GameController:

    def __init__(self, game, redPlayer, yellowPlayer):
        self.game = game
        self.redPlayer = redPlayer
        self.yellowPlayer = yellowPlayer
        self.trainingHistory = []
        self.player1Wins = 0
        self.player2Wins = 0
        self.draws = 0
        self.numberOfGames = 0

    def simulateManyGames(self, numberOfGames):
        self.numberOfGames = numberOfGames
        redPlayerWins = 0
        yellowPlayerWins = 0
        draws = 0
        for i in range(numberOfGames):
            self.game.resetBoard()
            self.playGame()

        totalWins = self.player1Wins + self.player2Wins
#         self.draws = 2000 - totalWins
#         return self.player1Wins
#         print(self.player1Wins)
#         print(self.player2Wins)
#         print(self.draws)
        self.draws = numberOfGames - totalWins
        
        print('Player 1 Wins: ' + str(int(self.player1Wins * 100 / numberOfGames)) + '%')
        print('Player 2 Wins: ' + str(int(self.player2Wins * 100 / numberOfGames)) + '%')
        print('Draws: ' + str((self.draws * 100 / numberOfGames)) + '%')
        print('Draws: ' + str(int(self.draws)))

        return self.player1Wins



    def playGame(self):
        playerToMove = self.redPlayer
        while len(self.game.game.get_moves()) > 0:
            availableMoves = self.game.getAvailableMoves()
            move = playerToMove.getMove(availableMoves, self.game.getBoard())
            self.game.move(move, playerToMove)
            if playerToMove.value == self.redPlayer.value:
                playerToMove = self.yellowPlayer
            else:
                playerToMove = self.redPlayer
        winner = 0
        if self.game.game.get_result(0) == 1:
            self.player1Wins += 1
            winner = -1
        if self.game.game.get_result(1) == 1:
            self.player2Wins += 1
            winner = 1
        if self.game.game.get_result(0) == 0:
            self.draws += 1
            
        for historyItem in self.game.getBoardHistory():
            self.trainingHistory.append((winner, historyItem))


    def getTrainingHistory(self):
        return self.trainingHistory


