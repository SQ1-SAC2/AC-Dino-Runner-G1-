import random

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.player = Dinosaur()

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            if random.randint(0, 2) == 2:
                self.obstacles.append(Bird())
            else:
                self.obstacles.append(Cactus())

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []
