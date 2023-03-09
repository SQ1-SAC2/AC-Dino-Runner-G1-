import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]

RUNNING_SNEAKERS = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Sneakers.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Sneakers.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_SNEAKERS = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpSneakers.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

DUCKING_SNEAKERS = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Sneakers.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Sneakers.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/Hammer.png'))
SNEAKERS = pygame.image.load(os.path.join(IMG_DIR, 'Other/Sneakers.png'))

DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))

DINO_FALL = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoFall.png"))
DINO_FALL_XL = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoFallXL.png"))
DINO_RUN_XL = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunXL.png"))
DINO_GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))
GAME_TITLE = pygame.image.load(os.path.join(IMG_DIR, "Other/GameTitle.png"))
RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

SELF_LOGO = pygame.image.load(os.path.join(IMG_DIR, "Other/SelfLogo.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
SNEAKERS_TYPE = "sneakers"

FONT_STYLE = [
    "freesansbold.ttf",
    "arial.ttf"
]
