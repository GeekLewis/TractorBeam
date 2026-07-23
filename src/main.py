import pygame
import shared.ships as ships
from settings import Settings
from pathlib import Path

root_path = Path(__file__).resolve().parent
game_icon = pygame.image.load(root_path / "assets" / "TractorBeamIcon.png")


def get_max_displayscale(game_width: int, game_height: int) -> int:
    sys_display = pygame.display.Info()
    max_h = int(sys_display.current_h / game_height)
    max_w = int(sys_display.current_w / game_width)
    return min(max_h, max_w)


def main():
    pygame.init()
    '''Init settings'''
    settings = Settings()
    
    '''Set the display'''
    display_scale = get_max_displayscale(settings.game_width, settings.game_height)
    pygame.display.set_icon(game_icon)
    screen = pygame.display.set_mode((
        settings.game_width * display_scale,
        settings.game_height * display_scale))
    pygame.display.set_caption("TractorBeam")
    game_surface = pygame.Surface((settings.game_width, settings.game_height))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    scaled = pygame.transform.scale(
        game_surface,(
            settings.game_width * display_scale,
            settings.game_height * display_scale
            )
        )
    screen.blit(scaled, (0,0))
    pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()