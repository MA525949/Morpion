from Models.Cell import Cell


class Board:

    def CreateCells(self):
        for i in range(self.column):
            for j in range(self.column):
                self.cells.append(Cell(i, j, self.CellSize, None))

    def __init__(self, column, CellSize):
        self.column = column
        self.cells = []
        self.CellSize = CellSize
        self.CreateCells()


    def FindCell(self, x, y):
        for cell in self.cells:
            if cell.x <= x <= cell.x+1 and self.CellSize*cell.y <= y <= self.CellSize*cell.y + cell.size:
                return cell


        print("apprend à cliquer au bon endroit")



