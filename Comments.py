from helpers import *
import pygame


class Comments:
    def __init__(self, text):
        self.text = text

    def read_comment_from_user(self):
        """
        Read the comment the user type.
        :return: string
            return typed comment
        """
        pressed_enter = False
        new_comment = ""
        # Draw the rectangle where the user can see the comment he typed
        draw_comment_text_box()
        while not pressed_enter:
            # get the string for comment
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    draw_comment_text_box()
                    if event.key == pygame.K_RETURN:
                        pressed_enter = True
                    # command to add len ! = 0
                    elif event.key == pygame.K_BACKSPACE \
                            and not (len(new_comment) == 0):
                        new_comment = new_comment[:-1]
                    else:
                        new_comment += event.unicode
                    font2 = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=False)
                    img2 = font2.render(new_comment, True, (50, 50, 50))
                    screen.blit(img2,
                                (VIEW_MORE_COMMENTS_X_POS + 1,
                                 VIEW_MORE_COMMENTS_Y_POS + 1))
                    pygame.display.update()
        return new_comment

    def display(self, comment_number):
        comment_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        comment_to_display = comment_font.render(self.text, True, (0, 0, 0))
        screen.blit(comment_to_display, (FIRST_COMMENT_X_POS,
                    FIRST_COMMENT_Y_POS + (comment_number * COMMENT_LINE_HEIGHT)))
