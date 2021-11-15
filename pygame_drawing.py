# Pygame_Drawing
# Author: Ubial
# 9 November 2021

# Get introduced to Pygame and draw objects on screen

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Pygame Drawing"

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        pygame.draw.rect(screen, (0, 90, 0), [0, 450, SCREEN_WIDTH, SCREEN_HEIGHT])

        leaf = pygame.Surface((150, 100))
        leaf.fill(WHITE)
        leaf.set_colorkey(WHITE)
        pygame.draw.ellipse(leaf, (0, 150, 0), [0, 0, 150, 100])
        screen.blit(pygame.transform.rotate(leaf, -45), (485, 360))
        screen.blit(pygame.transform.rotate(leaf, 45), (595, 360))

        pygame.draw.line(screen, (0, 150, 0), (625, 225), (625, 500), width=20)

        pygame.draw.circle(screen, BLACK, (600, 200), 80)
        pygame.draw.circle(screen, RED, (600, 200), 75)
        pygame.draw.circle(screen, BLACK, (600, 250), 80)
        pygame.draw.circle(screen, RED, (600, 250), 75)
        pygame.draw.circle(screen, BLACK, (650, 250), 80)
        pygame.draw.circle(screen, RED, (650, 250), 75)
        pygame.draw.circle(screen, BLACK, (650, 200), 80)
        pygame.draw.circle(screen, RED, (650, 200), 75)

        for i in range(5):
            pygame.draw.circle(screen, BLACK, (625, 225), 80-i*7)
            pygame.draw.circle(screen, RED, (625, 225), 75-i*7)
        pygame.draw.circle(screen, BLACK, (625, 225), 30)






        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
