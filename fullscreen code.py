from typing import Union

import pygame as pg
import time
import random

from pygame import Surface, SurfaceType

WIDTH, HEIGHT = 1000, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
screen_width, screen_height = WIN.get_size()
bg = pg.image.load("library/bg1.jpg")

Player_Width = 40
Player_Height = 60


def draw():
    screen_width, screen_height = WIN.get_size()
    scaled_image: Union[Surface, SurfaceType] = pg.transform.scale(bg, (screen_width,screen_height))
    WIN.blit(scaled_image, (0, 0))
    pg.display.update()


def main():
    pg.init()
    pg.display.set_caption("Snake")

    pg.Rect(200, screen_height - Player_Height, Player_Width, Player_Height)
    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

        draw()

    pg.quit()


if __name__ == "__main__":
    main()
