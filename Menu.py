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
        self.menubutton = Button(100, 100, 100, 100, "Hello World", (255, 255, 0), (0, 0, 0))

        # Create a piano:
        self.piano = Piano(pygame.mixer, self.width//2 - 110, 3*self.height//5)

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

                    if self.piano.is_clicked(mouseX, mouseY) and self.expected_note is not None:
                        self.actual_note = self.piano.get_played_note(self.expected_note)
                        self.actual_note.print_note()

                    if self.menubutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "menu"
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