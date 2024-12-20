import pygame
from modules.constants import *


pygame.init()
pygame.display.set_caption(GAME_NAME)

window = pygame.display.set_mode((WIDTH, HEIGHT))




if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
