import pygame
from stillenacht.star import Star
from stillenacht.canvas import Canvas


def test_should_change_color():
    value = False

    pygame.init()
    test_canvas_object = Canvas([400, 400])
    test_screen = test_canvas_object.draw_canvas()
    test_clock = pygame.time.Clock()

    test_star_list = []
    for test_star in range(20):
        test_star_object = Star(400, 400)
        test_star_list.append(test_star_object)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for star in test_star_list:
            star.blink(test_screen)

        test_canvas_object.flip()
        test_clock.tick(40)

    for j in range(len(test_star_list)-1):
        if test_star_list[j] != test_star_list[j+1]:
            value = True

    expected = True
    result = value
    assert expected == result


test_should_change_color()
