import pygame
from modules.constants import *


pygame.init()
pygame.display.set_caption(GAME_NAME)

window = pygame.display.set_mode((WIDTH, HEIGHT))

from modules.player import Player
from modules.fire import Fire
from modules.terrain import create_random_terrain, create_random_target_block
from modules.utils import get_background
from modules.collision import handle_move, check_congratulation_collision

def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()



def handle_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.jump_count < 2:
                player.jump()
    return True


# Handle camera scrolling
def handle_scrolling(player):
    # if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or \
    #    ((player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
    #     offset_x += player.x_vel
        
    """
    Calculate offset to center the camera on the player.
    """
    offset_x = player.rect.centerx - WIDTH // 2
    return offset_x



if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
