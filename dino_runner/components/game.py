import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score



from dino_runner.utils.constants import BG, DINO_START, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


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
        self.death_count = 0

    def run(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        
        pygame.quit()

    def start_game(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset()
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
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        self.playing = False
        self.death_count += 1
        if self.show_menu():
            self.score.score = 0

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_width = SCREEN_WIDTH // 2 
        half_screen_height = SCREEN_HEIGHT // 2
        menu_screen_width = half_screen_width - 200
        if not self.death_count:
            self.print_text("Welcome to the Dino Game!", 32, half_screen_width, half_screen_height +20)
            self.print_text("Press any key to start", 20, half_screen_width, half_screen_height +60)
        else:
            self.print_text("Game Over :(", 32, half_screen_width, half_screen_height +20)
            self.print_text(f"Actual Score: {self.score.score}", 20, menu_screen_width, 
                            half_screen_height + 80)
            self.print_text(f"Number of Deaths: {self.death_count}", 20, 
                            menu_screen_width -30, half_screen_height + 110)


        self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140))
        pygame.display.update()
        self.handle_menu_events()

    def print_text(self, message, size, text_x_position, text_y_position):
        font = pygame.font.Font(FONT_STYLE, size)
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
                self.start_game()
