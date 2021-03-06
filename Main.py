import pygame, sys, math
from pygame.locals import *

import globalvars
from Game import Game
from Menu import Menu
from Help import Help


def main():
    pygame.init()
    width = 800
    height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pianote")
    pygame.display.set_icon(pygame.image.load('Resources/note.png'))
    clock = pygame.time.Clock()

    globalvars.currentScene = "menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if globalvars.currentScene == "game":
            scene = Game(screen, width, height, clock)
            scene.run()

        if globalvars.currentScene == "menu":
            scene = Menu(screen, width, height, clock)
            scene.run()

        if globalvars.currentScene == "help":
            scene = Help(screen, width, height, clock)
            scene.run()



if __name__ == "__main__":
    main()