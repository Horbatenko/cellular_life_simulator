from classes.game_logic import Field
from classes import Graphics as G
import pygame
from settings import START_PAUSE_TIME, PAUSE_TIME_DELTA


class Game:

    def __init__(self, cellsRowsNum, cellsColsNum):
        self.grafics = G.Grafics(cellsRowsNum, cellsColsNum)
        self.genNewFields(cellsRowsNum, cellsColsNum)


    def run(self):
        pauseTime = START_PAUSE_TIME
        while True:
            if self.state:
                nowField = self.field
                nextField = self.field2
            else:
                nowField = self.field2
                nextField = self.field

            event = self.grafics.handleEvents()
            if event == 'pause':
                self.pause = not self.pause
            elif event == 'next' and self.pause:
                self.calculateGenerations(nowField, nextField)
                self.state = not self.state
            elif event == 'speed_up' and pauseTime - 100 > 0:
                pauseTime -= PAUSE_TIME_DELTA
            elif event == 'speed_down':
                pauseTime += PAUSE_TIME_DELTA
            elif event == 'new':
                self.genNewFields(self.field.height, self.field.width)

            self.grafics.reDraw(nowField.cells)

            pygame.time.wait(pauseTime)

            if not self.pause:
                self.calculateGenerations(nowField, nextField)
                self.state = not self.state

    def calculateGenerations(self, nowField, nextField):
        for row in nextField.cells:
            for cell in row:
                cell.state = nowField.cells[cell.position['x']][cell.position['y']].calculateState(nowField)

    def showFieldConsole(self):
        if self.state:
            fieldToShow = self.field.cells
        else:
            fieldToShow = self.field2.cells

        print('_____________________________________')

        for row in fieldToShow:
            strRow = ''
            for cell in row:
                if cell.state:
                    strRow += '*'
                else:
                    strRow += ' '
            print(strRow)

    def genNewFields(self, cellsRowsNum, cellsColsNum):
        self.field = Field.Field(cellsRowsNum, cellsColsNum, self.grafics.cellSize)
        self.field2 = Field.Field(cellsRowsNum, cellsColsNum, self.grafics.cellSize)
        self.state = True
        self.pause = True
