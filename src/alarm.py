import pygame
from src.config import ALARM_FILE


class Alarm:

    def __init__(self):
        try:
            print('before mixer')
            pygame.mixer.init(
                frequency=44100,
                size=-16,
                channels=2,
                buffer=512
            )
            print('after mixer')

            self.sound = pygame.mixer.Sound(ALARM_FILE)

        except pygame.error as e:
            print(f"Audio initialization failed: {e}")
            self.sound = None

        self.playing = False


    def update(self, drowsy):

        if drowsy and not self.playing and self.sound:

            self.sound.play(loops=-1)
            self.playing = True


        elif not drowsy and self.playing:

            pygame.mixer.stop()
            self.playing = False