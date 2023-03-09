import random
from pygame.sprite import Sprite
from pygame import Surface

from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self, image: Surface, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.type = type
        self.duration = random.randint(5, 8) #Tiempo de duración del power up
        self.start_time = 0 #Tiempo en el que fue tomado el power up

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))