'''This module is for holding the ship class and other ship information'''

from pygame import sprite
from pygame import Surface

class Ship(sprite.Sprite):
    '''
    This is a subclass of Sprite represting any moving ships in the game
    Attributes:
        x and y (int): these will give the starting x,y coordinates for
            the center of the ship
        images (dict): a dictionary of surfaces with the expected keys
            of "straight", "left", and "right". If there are no left/right
            roll images each key can point to the same straight down image
        enemy_is_down (bool): If true the front of the ship (top of the image)
            will point toward the bottom of the screen and advance down. 
            True will invert these. Default is True
    '''
    def __init__(self, x:int, y:int, images:dict[str, Surface], enemy_is_down:bool=True) -> None:
        super().__init__()
        self.images = images
        self.roll = "straight"
        self.image = self.images[self.roll]
        self.rect = self.image.get_rect(center=(x,y))
        self.enemy_is_down = enemy_is_down
        

        
