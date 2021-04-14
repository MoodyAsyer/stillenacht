import pygame
import random
from stillenacht.canvas import Canvas
from stillenacht.snow import Snow


def test_should_move():
    value = False

    pygame.init()
    test_canvas_object = Canvas([400, 400])
    test_screen = test_canvas_object.draw_canvas()
    test_clock = pygame.time.Clock()

    test_snow_list = []
    for snow in range(400//4):
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)
        test_snow_list.append([x, y])

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        test_canvas_object.set_bg_color()

        for i in range(len(test_snow_list)):
            snow_object = Snow(test_snow_list[i][0], test_snow_list[i][1])
            snow_object.draw(test_screen)
            test_snow_list[i][1] += random.randrange(1, 5)
            if test_snow_list[i][1] > 400:
                y = random.randrange(-50, -10)
                test_snow_list[i][1] = y
                x = random.randrange(0, 400)
                test_snow_list[i][0] = x

        test_canvas_object.flip()
        test_clock.tick(40)

    for i in range(len(test_snow_list)-1):
        if test_snow_list[i] != test_snow_list[i+1]:
            value = True

    expected = True
    result = value
    assert expected == result


test_should_move()
