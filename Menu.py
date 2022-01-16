import pygame, sys, math
from Piano import Piano
from Button import Button
from pygame.locals import *
import globalvars


class Menu:
    def __init__(self, screen, width, height, clock):

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
        
        # Create the button to the menu
        self.menubutton = Button(self.width//2-50, 4*self.height//5, 100, 100, "Play Game", (255, 255, 0), (0, 0, 0))

        # Create a piano:
        self.piano = Piano(pygame.mixer, self.width//2 - 110, 1*self.height//5)

        self.actual_note = None

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (50.2, 50.2, 50.2)

        self.running = True

    def run(self):

        # main loop
        while self.running:
            mouseX, mouseY = pygame.mouse.get_pos()
            left, right, middle = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Call the collision checking functions of the various objects:
                    left, right, middle = pygame.mouse.get_pressed()

                    if left:
                        self.piano.is_clicked(mouseX, mouseY)

                    if self.menubutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "game"
                        print(globalvars.currentScene)
                        self.running = False
                        break

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.piano.reset_color()

            self.screen.fill(self.white)


            # Draw the piano
            self.piano.draw(self.screen)

            # Draw the menu button
            self.menubutton.draw(self.screen)
            

            pygame.display.update()
            self.clock.tick(60)