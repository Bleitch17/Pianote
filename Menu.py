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
        
        # Create the button to the game
        self.gamebutton = Button(self.width//2, 3*self.height//5, 200, 100, "Play Game", (156, 219, 177), (0, 0, 0), 40)

        # Create the button to the help page
        self.helpbutton = Button(self.width//2, 4*self.height//5, 200, 100, "Help", (156, 219, 177), (0, 0, 0), 40)

        # Create a piano:
        self.piano1 = Piano(pygame.mixer, self.width//2 - 189, 1*self.height//5, 1)
        self.piano2 = Piano(pygame.mixer, self.width//2 - 0, 1*self.height//5, 1)

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
                        self.piano1.is_clicked(mouseX, mouseY)
                        self.piano2.is_clicked(mouseX, mouseY)

                    if self.gamebutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "game"
                        print(globalvars.currentScene)
                        self.running = False
                        break

                    if self.helpbutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "help"
                        print(globalvars.currentScene)
                        self.running = False
                        break

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.piano1.reset_color()
                    self.piano2.reset_color()

            self.screen.fill((194, 225, 231))


            # Draw the piano
            self.piano1.draw(self.screen)
            self.piano2.draw(self.screen)

            # Draw the menu button and game button
            self.gamebutton.draw(self.screen)
            self.helpbutton.draw(self.screen)

            # Draw title
            title = pygame.font.SysFont('Roboto', 100).render("Pianote", True, (0,0,0))
            self.screen.blit(title, title.get_rect(center = (self.width/2, self.height/7)))
             
            

            pygame.display.update()
            self.clock.tick(60)