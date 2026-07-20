from dataclasses import dataclass

@dataclass
class Settings:
    game_width: int = 720
    game_height: int = 360
    mothership_zone: int = 90
