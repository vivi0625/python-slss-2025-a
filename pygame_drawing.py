# Pygame Drawing
# Author: Ubial
# 5 January 2026

import pygame

def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    GREY  = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        # draw a red rectangle in the middle of the screen
        pygame.draw.rect(screen, RED, (WIDTH / 2 - 100, HEIGHT / 2 - 40, 200, 80))
        # TODO: draw a blue circle on top of the red rectangle
        # draw a 6 lines from the top middle to the right

        # draw a house
        pygame.draw.rect(screen, BLUE,(WIDTH / 7 - 100, HEIGHT / 2 - 40, 200, 80))
        pygame.draw.polygon(screen, GREY, [(100, 100), (200, 150), (150, 200)])



        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
