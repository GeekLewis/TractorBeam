'''This module is for holding the ship class and other ship information'''

import pygame

class Ship(pygame.sprite.Sprite):
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
    def __init__(self, x:int, y:int, images:dict[str, pygame.Surface],
                 enemy_is_down:bool=True) -> None:
        super().__init__()
        self.images = images
        self.roll = "straight"
        self.image = self.images[self.roll]
        self.rect = self.image.get_rect(center=(x,y))
        self.enemy_is_down = enemy_is_down
        self.hor_vel:int = 0
        self.ver_vel:int = 0


class EnemyShip(Ship):
    '''
    Subclass for most enemy ships.
    
    Additional Attrribute of grappled (default False) is used to indicate 
    if the ship is currently grappled by the player's tractor beam
    '''
    def __init__(self, x: int, y: int, images: dict[str, pygame.Surface],
                 enemy_is_down: bool = True) -> None:
        super().__init__(x, y, images, enemy_is_down)
        self.grappled:bool = False


class PlayerShip(Ship):
    '''
    Subclass for the player ship. 
    Automaticaly sets enemy_is_down to False
    
    Additional Attributes:
        shields(int): This is the current value of the ships shields
        shields_max(int): Defines that max shield level for recharging 
        weapon(object) the player's ship will be able to take differnt weapons
    '''
    def __init__(self, x: int, y: int, images: dict[str, pygame.Surface]) -> None:
        super().__init__(x, y, images, enemy_is_down=False)
        self.shields:int = 0
        self.shields_max:int = 0
        self.weapon:object