import pygame

if __name__ == "__main__":
    print("God I hope this works")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)

    c4 = pygame.mixer.Sound("Audio/c4.wav")
    e4 = pygame.mixer.Sound("Audio/e4.wav")
    g4 = pygame.mixer.Sound("Audio/g4.wav")

    c_channel = pygame.mixer.Channel(0)
    e_channel = pygame.mixer.Channel(1)
    g_channel = pygame.mixer.Channel(2)

    c_channel.play(c4, loops=0, maxtime=2000, fade_ms=125)
    e_channel.play(e4, loops=0, maxtime=2000, fade_ms=125)
    g_channel.play(g4, loops=0, maxtime=2000, fade_ms=125)

    while g_channel.get_busy():
        if not g_channel.get_busy:
            break


    pygame.mixer.quit()
    pygame.quit()