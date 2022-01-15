import pygame, sys, math
from pygame.locals import *


class Game:
    def __init__(self, width=100, height=100):

        # window parameters
        self.width = width
        self.height = height
        self.size = (width, height)
        # self.logo = pygame.image.load("<Relative Path>")
        # pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Basic-Ear-Trainer")

        # mouse variables
        self.left, self.middle, self.right = pygame.mouse.get_pressed()
        self.mouseX, self.mouseY = pygame.mouse.get_pos()

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # surfaces
        self.screen = pygame.display.set_mode(self.size)

        # game loop controls
        self.running = False
        self.clock = pygame.time.Clock()

    def run(self, r=True):

        self.running = r

        # main loop
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW




            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.screen.fill(self.white)

            pygame.draw.line(self.screen, self.black, (0,0), (pygame.mouse.get_pos()))

            


            pygame.display.update()
            self.clock.tick(60)