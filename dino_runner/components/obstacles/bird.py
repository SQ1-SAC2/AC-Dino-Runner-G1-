import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        self.type = "bird"
        self.step = 0
        if random.randint(0,2) == 0:
            self.bird_rect_y = 320
        elif random.randint(0,2) == 1:
            self.bird_rect_y = 220
        else:
            self.bird_rect_y = 270

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        image = BIRD[self.step // 10]
        self.image = image
        self.rect.y = self.bird_rect_y
        self.step +=1
        if self.step >= 20:
            self.step = 0
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.remove(self)