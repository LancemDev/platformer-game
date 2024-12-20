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


# Draw all game elements
def draw_frame(window, background, bg_image, player, objects, offset_x):
    """Draw all game elements"""
    window.fill((0, 0, 0))  # Clear the screen
    draw(window, background, bg_image, player, objects, offset_x)  # Player is drawn here
    pygame.display.update()
  
def display_congratulations(window):
    """Show the congratulatory message and reload the game after 3 seconds"""
    font = pygame.font.SysFont('Serif', 50)
    text = font.render("Congratulations! You've won!", True, (255, 255, 255))
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

    pygame.time.wait(3000)  # Wait for 3 seconds
    reload_game()  # Reload the game or restart the level

def reload_game():
    """Function to reload or restart the game"""
    # You can either reset the level or restart the entire game by reinitializing the main function
    main(window)



if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
