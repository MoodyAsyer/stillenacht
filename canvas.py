import pygame
#BLACK = [0,0,0]

class Canvas():
    def __init__(self,size):
        self.__size = size
        self.__color = [0,0,0]

    def draw_canvas(self):
        return pygame.display.set_mode(self.__size)

    def canvas_caption(self):
        pygame.display.set_caption("Stille nacht")

    def set_bg_color(self):
        self.draw_canvas().fill(self.__color)

    def flip(self):
        pygame.display.flip()

