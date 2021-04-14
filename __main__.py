import pygame
import random
import sys

from stillenacht.canvas import Canvas
from stillenacht.snow import Snow
from stillenacht.star import Star
from stillenacht.moon import Moon

if __name__ == '__main__':
    pygame.init()

    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except:
        width = 400
        height = 400

    size = [width, height]
    canvas_object = Canvas(size)
    screen = canvas_object.draw_canvas()
    caption = canvas_object.canvas_caption()

    clock = pygame.time.Clock()

    star_list = []
    for star in range(20):
        star_object = Star(width, height)
        star_list.append(star_object)

    snow_list = []
    for snow in range(width//4):
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        snow_list.append([x, y])

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        canvas_object.set_bg_color()

        moon_object = Moon.getinstance(width, height)
        moon_object.draw(screen)

        for star in star_list:
            star.blink(screen)

        for i in range(len(snow_list)):
            snow_object = Snow(snow_list[i][0], snow_list[i][1])
            snow_object.draw(screen)
            snow_list[i][1] += random.randrange(1, 5)
            if snow_list[i][1] > height:
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                x = random.randrange(0, width)
                snow_list[i][0] = x

        canvas_object.flip()
        clock.tick(40)

    pygame.quit()
