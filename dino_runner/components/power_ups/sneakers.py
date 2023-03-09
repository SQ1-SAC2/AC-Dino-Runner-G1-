from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SNEAKERS, SNEAKERS_TYPE


class Sneakers(PowerUp):
    def __init__(self):
        super().__init__(SNEAKERS, SNEAKERS_TYPE)