import pygame


from Game import Game


def main():
    pygame.init()

    MyApp = Game(250, 250)
    MyApp.run()

    pygame.quit()


if __name__ == "__main__":
    main()
