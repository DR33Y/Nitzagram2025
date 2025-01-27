import pygame
from constants import *
from helpers import screen


class Filter:
    def __init__(self, color, transparency_level):
        self.__color = color
        self.__transparency_level = transparency_level

    def apply_filter(self):
        surf = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        surf.fill(self.__color)
        surf.set_alpha(self.__transparency_level)
        screen.blit(surf, (POST_X_POS, POST_Y_POS))
