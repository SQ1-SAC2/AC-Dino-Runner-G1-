import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DEFAULT_TYPE, DINO_DEAD, DINO_FALL_XL, DINO_GAME_OVER, DINO_RUN_XL, FONT_STYLE, GAME_TITLE, HAMMER_TYPE, HEART, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, SELF_LOGO, SHIELD_TYPE, SNEAKERS_TYPE, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0


    def run(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        
        pygame.quit()

    def start_game(self):
        self.playing = True
        self.player.lifes = 1
        self.obstacle_manager.reset()
        self.power_up_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(
            self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(
            self.game_speed, self.score.score, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.check_power_up(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(HEART, (800, 50))
        self.print_text(f"Life: {self.player.lifes}", 0, 20, 900, 70)
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        is_shield_invincible = self.player.type == SHIELD_TYPE
        if not is_shield_invincible:
            if self.player.type == DEFAULT_TYPE:
                self.player.lifes -= 1
                if self.player.lifes == 0:
                    pygame.time.delay(1000)
                    self.playing = False
                    self.death_count += 1
                    self.handle_menu_events()
            elif self.player.type == HAMMER_TYPE:
                self.player.lifes += 1

    def show_menu(self):
        self.screen.fill((200, 200, 200))
        half_screen_width = SCREEN_WIDTH // 2 
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            self.screen.blit(DINO_RUN_XL, (-100, 100))
            self.screen.blit(GAME_TITLE, (half_screen_width - 80, half_screen_height - 140))
            self.screen.blit(SELF_LOGO, (950, 540))

            self.print_text("Press any key to start", 0, 20, 
                            half_screen_width +100, half_screen_height +20)
        else:
            self.screen.blit(DINO_FALL_XL, (0, 400))
            self.screen.blit(DINO_DEAD, (half_screen_width - 20, half_screen_height - 230))
            self.screen.blit(DINO_GAME_OVER, (half_screen_width - 180, half_screen_height - 130))
            self.screen.blit(RESET, (780, 450))

            self.print_text(f"Actual Score: {self.score.score}", 0, 20, 
                            half_screen_width, half_screen_height -50)
            self.print_text(f"High Score: {self.score.max_score}", 0, 20, 
                            half_screen_width, half_screen_height - 10)
            self.print_text(f"Number of Deaths: {self.death_count}", 0, 20, 
                            half_screen_width, half_screen_height + 30)
            self.print_text("Press any button to play again! ", 0, 20, 
                            820, 550)

        pygame.display.update()
        self.handle_menu_events()

    def print_text(self, message, font_type, size, text_x_position, text_y_position):
        font = pygame.font.Font(FONT_STYLE[font_type], size)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (text_x_position, text_y_position)
        self.screen.blit(text, text_rect)

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            if event.type == pygame.KEYDOWN:
                self.score.score = 0
                self.start_game()
