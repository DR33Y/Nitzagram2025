import pygame
from helpers import screen
from constants import *


class Post:
    def __init__(self, username, location, description, likes_counter, comments):
        self.__username = username
        self.__location = location
        self.__description = description
        self.__likes_counter = likes_counter
        self.__comments = comments

    def add_like(self):
        self.__likes_counter += 1

    def add_comment(self, text):
        self.__comments.append(text)

    def display(self):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)

        username_text = font.render(f"{self.__username}", True, BLACK)
        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))

        location_text = font.render(f"{self.__location}", True, GREY)
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        likes_text = font.render(f"Liked by {self.__likes_counter} users", True, BLACK)
        screen.blit(likes_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        description_text = font.render(f"{self.__description}", True, BLACK)
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
