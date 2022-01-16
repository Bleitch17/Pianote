import pygame, sys, math
from Piano import Piano
from Button import Button
from pygame.locals import *
import globalvars


class Help:
    def __init__(self, screen, width, height, clock):

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
        
        # Create the button to the menu
        self.menubutton = Button(self.width//2, 1*self.height//2, 250, 100, "Return to Menu", (156, 219, 177), (0, 0, 0), 40)


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

                    if self.menubutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "menu"
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

            # Draw the menu button
            self.menubutton.draw(self.screen)

            # Draw title
            title = pygame.font.SysFont('Roboto', 100).render("Pianote", True, (0,0,0))
            self.screen.blit(title, title.get_rect(center = (self.width/2, self.height/7)))

            # Write help text
            helpText = ["Pianote is a program to help practice piano Ear Training", 
                        "Press the New Note button to listen to a new note",
                        "Then, press the corresponding key on the Piano keyboard",
                        "The accuracy meter will show how close your note was to the actual note",
                        "If neccessary, press the Replay Note button to listen to the current note again"]

            for lineIndex in range(len(helpText)):
                line = pygame.font.SysFont('Roboto', 30).render(helpText[lineIndex], True, (0,0,0))
                self.screen.blit(line, line.get_rect(center = (self.width/2, 6*self.height/10 + lineIndex*50)))
            

            pygame.display.update()
            self.clock.tick(60)