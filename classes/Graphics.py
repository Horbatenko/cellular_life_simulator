import pygame
from pygame import *
from settings import *

class Grafics:

    def __init__(self, cellsRowsNum, cellsColsNum):

        if cellsRowsNum > cellsColsNum or cellsRowsNum == cellsColsNum:

            self.cellSize = CELLS_FIELD_HEIGHT / cellsRowsNum
        else:
            self.cellSize = CELLS_FIELD_WIDTH / cellsColsNum

        SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("John Conway's Game of Life")

        self.bg = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg.fill(Color("#ffffff"))


        self.field = Surface((CELLS_FIELD_WIDTH, CELLS_FIELD_HEIGHT))
        self.field.fill(Color("#f7f7f7"))


    def handleEvents(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == 32:#space
                    return 'pause'
                elif e.key == 275:#arrow right
                    return 'next'
                elif e.key == 273:#arrow up
                    return 'speed_up'
                elif e.key == 274:#arrow down
                    return 'speed_down'
                elif e.key == 13:
                    return 'new'




    def reDraw(self, cells):
        self.field.fill(Color('#f7f7f7'))
        y = 0
        for row in cells:
            x = 0
            for cell in row:
                if cell.state:
                    self.field.blit(cell.image, (x, y))
                else:
                    pygame.draw.rect(self.field, Color("#f7f7f7"), pygame.Rect(x, y, self.cellSize, self.cellSize))
                x += self.cellSize
            y += self.cellSize

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.field, (0, 0))
        pygame.display.update()