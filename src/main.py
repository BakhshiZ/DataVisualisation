"""
* Initialize and render the GUI using Pygame.
* Handle user input (e.g., placing start/end points, barriers).
* Call the appropriate pathfinding algorithm (BFS, DFS, Dijkstra, A*).
* Visualize the algorithm's progress and final path.
"""

import pygame
from utils.constants import *
from utils.grid import *

pygame.init()
game_grid = create_grid()

button_surface = pygame.Surface((BUTTON_WIN_WIDTH, BUTTON_WIN_HEIGHT))
game_surface = pygame.Surface((GAME_WIN_WIDTH, GAME_WIN_HEIGHT))
master_screen = pygame.display.set_mode((GAME_WIN_WIDTH, GAME_WIN_HEIGHT + BUTTON_WIN_HEIGHT))

pygame.display.set_caption("Searching algorithms by BakhshiZ")


buttonFont = pygame.font.SysFont('Arial', 20)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    button_surface.fill(COLOURS["BGCOLOUR"])

    # Define button positions and properties
    button_spacing = 10
    button_width = BUTTON_WIDTH
    button_height = 40
    button_y = 5

    mouse_pos = pygame.mouse.get_pos()

    for i in range(4):
        button_x = 70 + i * (button_spacing + button_width)
        rect = pygame.Rect(button_x, button_y, button_width, button_height)

        # Check if mouse is hovering over the button
        if rect.collidepoint(mouse_pos):
            color = COLOURS["BUTTON_LIGHT"]
        else:
            color = COLOURS["BUTTON_NORMAL"]

        pygame.draw.rect(button_surface, color, rect, border_radius=10)

        match i:
            case 0:
                a_star_text = buttonFont.render('A*', True, COLOURS["TEXT"])
                a_star_text_rect = a_star_text.get_rect(center=rect.center)
                button_surface.blit(a_star_text, a_star_text_rect)

            case 1:
                bfs_text = buttonFont.render('BFS', True, COLOURS["TEXT"])
                bfs_text_rect = bfs_text.get_rect(center=rect.center)
                button_surface.blit(bfs_text, bfs_text_rect)

            case 2:
                dfs_text = buttonFont.render('DFS', True, COLOURS["TEXT"])
                dfs_text_rect = dfs_text.get_rect(center=rect.center)
                button_surface.blit(dfs_text, dfs_text_rect)

            case 3:
                dijkstra_text = buttonFont.render('Dijkstra', True, COLOURS["TEXT"])
                dijkstra_text_rect = dijkstra_text.get_rect(center=rect.center)
                button_surface.blit(dijkstra_text, dijkstra_text_rect)

    master_screen.blit(button_surface, (0, 0))
    master_screen.blit(game_surface, (0, BUTTON_WIN_HEIGHT))

    pygame.display.update()

pygame.quit()
"""
---------------------
|A*|BFS|DFS|Dijkstra|
---------------------
|                   |
|                   |
|                   |
|                   |
|                   |
---------------------
"""
