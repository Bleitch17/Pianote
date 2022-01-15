import pygame


class Note:
    def __init__(self, mixer, symbol='c', octave=4):
        self.mixer = mixer
        self.symbol = symbol
        self.octave = octave

        self.name = symbol + str(octave)
        self.sound = mixer.Sound("Audio/" + f"{self.name}" + ".wav")

    def play(self):
        self.mixer.Channel(0).play(self.sound)
        while self.mixer.Channel(0).get_busy:
            if not self.mixer.Channel(0).get_busy:
                break
