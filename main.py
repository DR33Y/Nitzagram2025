from ImagePost import ImagePost
from Comments import *
from buttons import comment_button
from Filter import Filter


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    purple_filter = Filter((30, 12, 121), 80)
    comments = []
    img_post = ImagePost("Daniel Ross", "Beer-Sheva", "Some Text...",
                         6, comments, 'Images/ronaldo.jpg', purple_filter)

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(comment_button, pygame.mouse.get_pos()):
                    new_text = read_comment_from_user()
                    new_comment = Comments(new_text)
                    img_post.add_comment(new_comment)
                    img_post.display_comments()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        img_post.display()
        img_post.display_comments()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
