import pygame


class Game:
    def __init__(self, width=100, height=100):

        # window parameters
        self.screen_w = width
        self.screen_h = height
        self.size = (width, height)
        # self.logo = pygame.image.load("<Relative Path>")
        # pygame.display.set_icon(self.logo)
        # pygame.display.set_caption("Snake")

        # mouse variables
        self.mouse_x = 0
        self.mouse_y = 0

        # colors
        self.black = 0, 0, 0
        self.white = 255, 255, 255

        # surfaces
        self.screen = pygame.display.set_mode(self.size)

        # game loop controls
        self.running = False
        self.clock = pygame.time.Clock()

    def run(self, r=True):

        # variable controlling main loop
        self.running = r

        # main loop
        while self.running:
            # ALL EVENT PROCESSING GOES BELOW

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.screen.fill(self.white)

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(60)