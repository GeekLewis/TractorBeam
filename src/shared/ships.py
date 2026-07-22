'''This module is for holding the ship class and other ship information'''

from pygame import sprite
from pygame import Surface

class Ship(sprite.Sprite):
    def __init__(self, x:int, y:int, images:dict[str, Surface], enemy_is_down:bool=True) -> None:
        self.images = images
        self.roll = "straight"
        self.image = self.images[self.roll]
        self.rect = self.image.get_rect(center=(x,y))
        self.enemy_is_down = enemy_is_down
        self.alive

        
