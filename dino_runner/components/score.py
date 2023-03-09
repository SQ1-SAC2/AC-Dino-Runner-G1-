import pygame
from dino_runner.components.dinosaur import Dinosaur

from dino_runner.utils.constants import FONT_STYLE, SNEAKERS_TYPE


class Score:
    def __init__(self):
        self.score = 0
        self.max_score = 0

        self.player = Dinosaur()

    def update(self, game):
        if not self.player.type == SNEAKERS_TYPE:
            self.score += 1
        else:
            self.score += 4

        if self.score % 500 == 0:
            game.game_speed += 4

        if self.score >= self.max_score:
            self.max_score = self.score

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE[0], 24)
        text = font.render(f"Score: {self.score}; Max Score: {self.max_score}", True, (0 ,0 ,0))
        text_rect = text.get_rect()
        text_rect.center = (900, 30)
        screen.blit(text, text_rect)
    


