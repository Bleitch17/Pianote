import pygame, sys, math
from pygame.locals import *


from Game import Game


def main():
    pygame.init()
    width = 800
    height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Basic-Ear-Trainer")
    clock = pygame.time.Clock()

    currentScene = "game"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if currentScene == "game":
            scene = Game(screen, width, height, clock)
            scene.run()



if __name__ == "__main__":
    main()