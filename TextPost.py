import pygame
from helpers import screen
from constants import *
from Post import Post


class TextPost(Post):
    def __init__(self, username, location, description, likes_counter, comments, text, text_color, background_color):
        super().__init__(username, location, description, likes_counter, comments)
        self.__text = text
        self.__text_color = text_color
        self.__background_color = background_color

    def display(self):
        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        text = font.render(self.__text, True, self.__text_color)
        rectangle = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.__background_color, rectangle)
        screen.blit(text, (POST_X_POS, POST_Y_POS))
        super().display()