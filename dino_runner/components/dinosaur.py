
import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, DUCKING_SNEAKERS, FONT_STYLE, HAMMER, HAMMER_TYPE, JUMPING_HAMMER, JUMPING_SHIELD, JUMPING_SNEAKERS, RUNNING, JUMPING, DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, RUNNING_SNEAKERS, SCREEN_WIDTH, SHIELD, SHIELD_TYPE, SNEAKERS, SNEAKERS_TYPE


DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING =  "ducking"

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, SNEAKERS_TYPE: DUCKING_SNEAKERS}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, SNEAKERS_TYPE: JUMPING_SNEAKERS}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, SNEAKERS_TYPE: RUNNING_SNEAKERS}


class Dinosaur(Sprite):
    POSITION_X = 80
    POSITION_Y = 310
    DUCK_POSITION_Y = 343
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.update_image(RUN_IMG[self.type][0])
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.lifes = 1

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()
        
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def duck(self):
        self.update_image(
            DUCK_IMG[self.type][self.step // 5], pos_y = self.DUCK_POSITION_Y) 
        self.step += 1

    def jump(self):
        pos_y = self.rect.y - self.jump_velocity * 4
        self.update_image(JUMP_IMG[self.type], pos_y = pos_y)    
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POSITION_Y
        
        if self.rect.y > self.POSITION_Y:
            self.action = DINO_RUNNING

    def run(self):
        self.update_image(RUN_IMG[self.type][self.step // 5])
        self.step += 1

    def update_image(self, image: pygame.Surface, pos_x = None, pos_y = None):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x or self.POSITION_X
        self.rect.y = pos_y or self.POSITION_Y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + \
            (power_up.duration * 1000)

    def check_power_up(self, screen):
        self.screen = screen
        if self.type == SHIELD_TYPE:
            self.draw_power_up(screen, "Shield", SHIELD, 20, (0, 0, 0), SCREEN_WIDTH // 2, 50)
        elif self.type == SNEAKERS_TYPE:
            self.draw_power_up(screen, "Sneakers", SNEAKERS, 20, (0, 0, 0), SCREEN_WIDTH // 2, 50)
        elif self.type == HAMMER_TYPE:
            self.draw_power_up(screen, "Hammer", HAMMER, 20, (0, 0, 0), SCREEN_WIDTH // 2, 50)

    def draw_power_up(self, screen, power_up_name, surface, font_size, color, x_pos, y_pos):
        time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
        if time_to_show >= 0:
            font = pygame.font.Font(FONT_STYLE[0], font_size)
            text = font.render(f"{power_up_name} enabled for {time_to_show} seconds", True, (color))
            text_rect = text.get_rect()
            text_rect.center = (x_pos, y_pos)
            screen.blit(text, text_rect)
            self.screen.blit(surface, (x_pos, y_pos +20))
        else:
            self.type = DEFAULT_TYPE
            self.power_up_time_up = 0