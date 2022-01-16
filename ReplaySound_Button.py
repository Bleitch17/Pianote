import pygame

class replaySound_Button:

    width = 75
    height = 75

    def __init__(self, x=30, y=30):

        self.image_path = 'Resources/replay_button.png'
        self.x_pos = x
        self.y_pos = y

        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (replaySound_Button.width, replaySound_Button.height))
        self.collision_box = pygame.Rect(self.x_pos, self.y_pos, replaySound_Button.width, replaySound_Button.height)

    def draw(self, screen):
        screen.blit(self._image, (self.x_pos, self.y_pos))

    def is_pressed(self, event) -> bool:
        if self.collision_box.collidepoint(event.pos):
            return True
        return False

    def play_sound(self, Note):
        note_name = Note.print_note()
        print(f"ReplaySound button clicked! Now playing...{note_name}")
        
