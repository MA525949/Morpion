from Models.Board import Board
from Models.Player import Player
from Views.BoardView import BoardView


class GameController:
    def __init__(self, column, size):
        self.column = column
        self.size = size
        self.players : list = []
        self.board = Board(self.column, self.size)
        self.boardView = BoardView(self.board)
        self.currentPlayer = None

    def AddPlayer(self, player : Player):
        self.players.append(player)
        if self.currentPlayer is None:
            self.currentPlayer = self.players[0]

    def StartGame(self):
        self.boardView.DrawBoard()

    def SwitchNextPlayer(self):
        for i in range (len(self.players)):
            if self.players[i].ID == self.currentPlayer.ID:
                self.currentPlayer = self.players[(i+1) % len(self.players)]
                return

    def IsWinnerColumn(self, alignment):
        for player in self.players:
            for line in range (self.column):
                FollowingCounter = 0
                for column in range (self.column):
                    if self.board.FindCell(line, column).playerid == player.ID:
                        FollowingCounter += 1
                    else:
                        FollowingCounter = 0

                    if FollowingCounter == alignment:
                        return player

    def IsWinnerRow(self, alignment):
        for player in self.players:
            for line in range (self.column):
                FollowingCounter = 0
                for column in range (self.column):
                    if self.board.FindCell(column, line).playerid == player.ID:
                        FollowingCounter += 1
                    else:
                        FollowingCounter = 0

                    if FollowingCounter == alignment:
                        return player
    def IsWinnerDiag1(self, alignment):
        for player in self.players:
            for line in range (self.column):
                FollowingCounter = 0
                for column in range (self.column):
                    if line - column >= 0:
                        if self.board.FindCell(column , line - column ).playerid == player.ID:
                            FollowingCounter += 1
                        else:
                            FollowingCounter = 0
                    else:
                        FollowingCounter = 0
                    if FollowingCounter == alignment:
                        return player

    def IsWinnerDiag2(self, alignment):
        for player in self.players:
            for line in range(self.column):
                FollowingCounter = 0
                for column in range(self.column):
                    if line + column < self.column:
                        if self.board.FindCell(column, line + column).playerid == player.ID:
                            FollowingCounter += 1
                        else:
                            FollowingCounter = 0
                    else :
                        FollowingCounter = 0
                    if FollowingCounter == alignment:
                        return player

# je clique et je joue mon tour
    def TryPlay(self, x, y):
        cell = self.board.FindCell(x//self.size, y//self.size)
        if not cell.IsTaken():
            self.boardView.UpdateCell(self.currentPlayer, cell)
            self.currentPlayer.listcoup.append(int((cell.y / self.size) * self.column + cell.x / self.size))
            cell.playerid = self.currentPlayer.ID
            self.SwitchNextPlayer()










