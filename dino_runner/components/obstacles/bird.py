import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        if random.randint(0, 1) == 0:
            self.rect.y = 90
        else:
            self.rect.y = 120

        self.step = 0

    def draw(self, screen):
        if self.step >= 10:
            self.step = 0
        screen.blit(self.image[self.step // 5], (self.rect.x, self.rect.y))
        self.step += 1



        

    