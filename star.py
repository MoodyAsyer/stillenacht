import pygame
import random
from stillenacht.drawable_abstract import Abstract


# YELLOW = [255,255,0]
# RED = [255,0,0]

class Star(Abstract):
    def __init__(self, x, y):
        self.__x = random.randrange(1, x)
        self.__y = random.randrange(1, y)
        self.__color = [[255, 255, 0], [255, 0, 0]]
        self.__size = 1
        self.count = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.__color[self.count % 2], [self.__x, self.__y], self.__size)

    def blink(self, screen):
        self.count += 1
        self.draw(screen)
