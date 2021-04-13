
class GameController:

    def __init__(self, game, player1, player2):
        self.game = game
        self.player1 = player1
        self.player2 = player2
        self.trainingHistory = []
        self.player1Wins = 0
        self.player2Wins = 0
        self.draws = 0
        self.numberOfGames = 0

    def simulateManyGames(self, numberOfGames):
        self.numberOfGames = numberOfGames
        for i in range(numberOfGames):
            self.game.resetBoard()
            self.playGame()

        totalWins = self.player1Wins + self.player2Wins

        self.draws = numberOfGames - totalWins
        
        print('Player 1 Wins: ' + str((self.player1Wins * 100 / numberOfGames)) + '%')
        print('Player 2 Wins: ' + str((self.player2Wins * 100 / numberOfGames)) + '%')
        print('Draws: ' + str((self.draws * 100 / numberOfGames)) + '%')

    def playGame(self):
        
        playerToMove = self.player1
        while len(self.game.game.get_moves()) > 0:
            availableMoves = self.game.getAvailableMoves()
            move = playerToMove.getMove(availableMoves, self.game.getBoard())
            self.game.move(move, playerToMove)
            if playerToMove.value == self.player1.value:
                playerToMove = self.player2
            else:
                playerToMove = self.player1
        winner = 0
        if self.game.game.get_result(0) == 1:
            self.player1Wins += 1
            winner = -1
        elif self.game.game.get_result(1) == 1:
            self.player2Wins += 1
            winner = 1
        elif self.game.game.get_result(0) == 0:
            self.draws += 1
        for historyItem in self.game.getBoardHistory():
            self.trainingHistory.append((winner, historyItem))


    def getTrainingHistory(self):
        return self.trainingHistory


