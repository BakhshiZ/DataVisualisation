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
grid = create_grid()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Searching algorithms by BakhshiZ")
screen.fill(COLOURS['BGCOLOUR'])
buttonFont = pygame.font.SysFont('Arial', 20)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing gridlines
    for i in range(PLAYABLE_ROWS):
        pygame.draw.line(screen, COLOURS["GRIDLINES"], (70 + i * 10, 60), (70 + i * 10, WIN_HEIGHT - 10))
    for j in range(PLAYABLE_COLUMNS):
        pygame.draw.line(screen, COLOURS["GRIDLINES"], (70, 60 + j * 10), (WIN_WIDTH - 60, 60 + j * 10))

    mouse_pos = pygame.mouse.get_pos()

    # Drawing and colouring all 4 buttons
    pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((70, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)
    pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((80 + (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)),
                     border_radius=10)
    pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((90 + 2 * (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)),
                     border_radius=10)
    pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((100 + 3 * (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)),
                     border_radius=10)

    if (70 <= mouse_pos[0] <= (70 + BUTTON_WIDTH)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((70, 5), (BUTTON_WIDTH, 40)), border_radius=10)

    elif ((80 + BUTTON_WIDTH) <= mouse_pos[0] <= (80 + 2 * BUTTON_WIDTH)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((80 + BUTTON_WIDTH, 5), (BUTTON_WIDTH, 40)),
                         border_radius=10)

    elif ((90 + 2 * BUTTON_WIDTH) <= mouse_pos[0] <= (90 + 3 * BUTTON_WIDTH)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((90 + 2 * BUTTON_WIDTH, 5), (BUTTON_WIDTH, 40)),
                         border_radius=10)

    elif ((100 + 3 * BUTTON_WIDTH) <= mouse_pos[0] <= (100 + 4 * BUTTON_WIDTH)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((100 + 3 * BUTTON_WIDTH, 5), (BUTTON_WIDTH, 40)),
                         border_radius=10)

    # Adding labels to buttons
    a_star_text = buttonFont.render('A*', True, COLOURS["TEXT"])
    a_star_width = (140 + BUTTON_WIDTH) // 2

    bfs_text = buttonFont.render('BFS', True, COLOURS["TEXT"])
    bfs_width = (160 + 2.8 * BUTTON_WIDTH) // 2

    dfs_text = buttonFont.render('DFS', True, COLOURS["TEXT"])
    dfs_width = (180 + 4.8 * BUTTON_WIDTH) // 2

    dijkstra_text = buttonFont.render('Dijkstra', True, COLOURS["TEXT"])
    dijkstra_width = (200 + 6.6 * BUTTON_WIDTH) // 2

    screen.blit(a_star_text, (a_star_width, TEXT_BUTTON_HEIGHT))
    screen.blit(bfs_text, (bfs_width, TEXT_BUTTON_HEIGHT))
    screen.blit(dfs_text, (dfs_width, TEXT_BUTTON_HEIGHT))
    screen.blit(dijkstra_text, (dijkstra_width, TEXT_BUTTON_HEIGHT))

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
