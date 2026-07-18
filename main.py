import pygame
from settings import Settings

pygame.init()

'''Init settings'''
settings = Settings()

'''Set the display'''
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

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