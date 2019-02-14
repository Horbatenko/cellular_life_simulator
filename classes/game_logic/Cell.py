import pygame
import os
import random


class Cell:

    def __init__(self, position, size, state=False):
        self.state = bool(state)
        sprites = os.listdir('./sprites')
        self.image = pygame.image.load('./sprites/' + random.choice(sprites))
        self.image = pygame.transform.scale(self.image, (int(size), int(size)))
        self.position = {'x': position['x'], 'y': position['y']}

    def calculateState(self, field):
        neirsNum = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                posX = self.position['x'] + i
                posY = self.position['y'] + j
                if field.height - 1 >= posX >= 0 and field.width - 1 >= posY >= 0:
                    neirsNum += int(field.cells[posX][posY].state)

        neirsNum -= int(self.state)

        if not self.state and neirsNum == 3:
            return True
        elif self.state and (neirsNum > 3 or neirsNum < 2):
            return False
        else:
            return self.state
