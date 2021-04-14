import pygame
from stillenacht.drawable_abstract import Abstract


# WHITE = [255,255,255]

class Snow(Abstract):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__color = [255, 255, 255]
        self.__size = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.__color, [self.x, self.y], self.__size)
