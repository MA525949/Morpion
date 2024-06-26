from Models.Board import Board
from Models.Cell import Cell
import pygame

from Models.Player import Player

WHITE = (255, 255, 255)


class BoardView:
    def __init__(self, board : Board):
        self.board = board
        self.CellSize = self.board.cells[0].size
        self.Column = self.board.column
        self.screen = pygame.display.set_mode(( self.CellSize* self.Column, self.CellSize * self.Column))

    def DrawBoard(self):
        for i in range(1, self.Column):
            pygame.draw.line(self.screen, WHITE, (0, self.CellSize * i), (self.CellSize * self.Column, self.CellSize * i))

        for i in range(1, self.Column):
            pygame.draw.line(self.screen, WHITE, (self.CellSize * i, 0), (self.CellSize * i, self.CellSize * self.Column))
        pygame.display.update()

    def DrawCross(self, COLOR, Cell : Cell):
        CrossPosition = self.CellSize/4
        Cell_x = Cell.x * self.CellSize
        Cell_y = Cell.y * self.CellSize
        pygame.draw.line(self.screen, COLOR, (Cell_x+CrossPosition, Cell_y + CrossPosition), (Cell_x+3*CrossPosition, Cell_y + 3*CrossPosition))
        pygame.draw.line(self.screen, COLOR, (Cell_x + 3*CrossPosition, Cell_y + CrossPosition),
                         (Cell_x +  CrossPosition, Cell_y + 3 * CrossPosition))
        pygame.display.flip()

    def DrawCircle(self, COLOR, Cell : Cell):
        CellSize = Cell.size
        CellCenter = CellSize/2
        Cell_x = Cell.x * self.CellSize
        Cell_y = Cell.y * self.CellSize
        pygame.draw.circle(self.screen, COLOR, (Cell_x+CellCenter, Cell_y + CellCenter), CellCenter/2, 5)
        pygame.display.flip()

    def UpdateCell(self, Player : Player, Cell : Cell):
        if Player.PawnType == 0:
            self.DrawCross(Player.color, Cell)
        if Player.PawnType == 1:
            self.DrawCircle(Player.color, Cell)
