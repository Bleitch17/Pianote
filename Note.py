import pygame


class Note:
    note_symbol_list = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

    def __init__(self, mixer, symbol='c', octave=4) -> None:
        self.mixer = mixer
        self.symbol = symbol
        self.octave = octave

        self.channel_num = self.find_channel_num()

        self.name = symbol + str(octave)
        self.sound = mixer.Sound("Audio/" + f"{self.name}" + ".wav")

    def find_channel_num(self) -> int:
        for symbol in Note.note_symbol_list:
            if symbol == self.symbol:
                return Note.note_symbol_list.index(symbol)

    def play(self, maxtime=4000, fade_ms=125) -> None:
        self.mixer.Channel(self.channel_num).play(self.sound, loops=0, maxtime=maxtime, fade_ms=fade_ms)

    def playing(self) -> bool:
        return self.mixer.Channel(self.channel_num).get_busy()

