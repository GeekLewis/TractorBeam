import pygame
from settings import Settings
from pathlib import Path

root_path = Path(__file__).resolve().parent
game_icon = pygame.image.load(root_path / "src" / "assets" / "TractorBeamIcon.png")

pygame.init()

'''Init settings'''
settings = Settings()

'''Set the display'''
pygame.display.set_icon(game_icon)
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("TractorBeam")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def main():
    print("Hello from tractorbeam!")


if __name__ == "__main__":
    main()

pygame.quit()