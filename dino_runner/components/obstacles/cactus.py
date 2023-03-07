import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        if random.randint(0,1) == 0:
            cactus_type = random.randint(0,2)
            image = SMALL_CACTUS[cactus_type]
            cactus_y = 325
        else:
            cactus_type = random.randint(0,2)
            image = LARGE_CACTUS[cactus_type]
            cactus_y = 300
        
        super().__init__(image)
        self.rect.y = cactus_y