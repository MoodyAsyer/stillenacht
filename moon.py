import pygame
from stillenacht.drawable_abstract import Abstract


# MOON_COLOR = [220,230,250]

class Moon(Abstract):
    __instance = None

    def __init__(self, x, y):
        self.__x = x - (x // 4)
        self.__y = y - (3 * (y // 4))
        self.__color = [220, 230, 250]
        self.__size = 60

        if Moon.__instance == None:
            Moon.__instance = self
        else:
            raise Exception("It is singleton")

    @staticmethod
    def getinstance(x, y):
        if Moon.__instance == None:
            return Moon(x, y)
        else:
            return Moon.__instance

    def draw(self, screen):
        pygame.draw.circle(screen, self.__color, [self.__x, self.__y], self.__size)
