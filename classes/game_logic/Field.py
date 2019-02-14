import random
from classes.game_logic import Cell


class Field:

    def __init__(self, height, width, cellSize):
        self.width = width
        self.height = height
        self.cells = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(Cell.Cell({'x': i, 'y': j}, cellSize))
            self.cells.append(row)

        self.fillFieldRandomStates()

    def fillFieldRandomStates(self):
        for row in self.cells:
            for cell in row:
                cell.state = random.choice([True,False])

    def fillByCellsNums(self, aliveCellsNums):
        cellsCounter = 0
        for row in self.cells:
            for cell in row:
                if cellsCounter in aliveCellsNums:
                    cell.state = True
                cellsCounter += 1

