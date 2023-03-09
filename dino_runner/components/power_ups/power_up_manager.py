import random
import pygame

from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.sneakers import Sneakers
from dino_runner.utils.constants import DEFAULT_TYPE


class PowerUpManager:
    def __init__(self) -> None:
        self.power_ups: list[PowerUp] = []
        #puntaje en el que se generará un power up
        self.when_appears = 0

    def update(self, game_speed, score, player):
        if not self.power_ups and score == self.when_appears:
            self.when_appears += random.randint(300, 400)
            power_up_ = random.randint(0, 2)
            if power_up_== 0:
                self.power_ups.append(Shield())
            elif power_up_ == 1:
                self.power_ups.append(Sneakers())
            else:
                self.power_ups.append(Hammer())         

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.type = DEFAULT_TYPE
        self.power_ups = []
        self.when_appears = random.randint(300, 400)