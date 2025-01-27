from helpers import *
from constants import *


class Post:
    def __init__(self, username, location, description, likes_counter, comments):
        self.__username = username
        self.__location = location
        self.__description = description
        self.__likes_counter = likes_counter
        self.__comments = comments
        self.__comments_display_index = 0

    def add_like(self):
        self.__likes_counter += 1

    def add_comment(self, text):
        self.__comments.append(text)

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.__comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.__comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.__comments)):
            if position_index >= len(self.__comments):
                position_index = 0
            self.__comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

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
