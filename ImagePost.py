import pygame.image
from helpers import screen
from constants import *
from Post import Post


class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments, img_path):
        super().__init__(username, location, description, likes_counter, comments)
        self.__img = pygame.image.load(img_path)
        self.__img = pygame.transform.scale(self.__img, (POST_WIDTH, POST_HEIGHT))

    def display(self):
        screen.blit(self.__img, (POST_X_POS, POST_Y_POS))
        super().display()
