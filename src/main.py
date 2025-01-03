"""
* Initialize and render the GUI using Pygame.
* Handle user input (e.g., placing start/end points, barriers).
* Call the appropriate pathfinding algorithm (BFS, DFS, Dijkstra, A*).
* Visualize the algorithm's progress and final path.
"""

import pygame
from utils.constants import *

pygame.init()
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
    for i in range(116):
        pygame.draw.line(screen, COLOURS["GRIDLINES"], (70 + i * 10, 60), (70 + i * 10, WIN_HEIGHT - 10))
        for j in range(72):
            pygame.draw.line(screen, COLOURS["GRIDLINES"], (70, 60 + j * 10), (WIN_WIDTH - 60, 60 + j * 10))

    mouse_pos = pygame.mouse.get_pos()

    # Drawing and colouring buttons
    if (70 <= mouse_pos[0] <= (70 + (WIN_WIDTH - 160) // 4)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((70, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)
    else:
        pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((70, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)

    if ((80 + (WIN_WIDTH - 160) // 4) <= mouse_pos[0] <= (80 + 2 * (WIN_WIDTH - 160) // 4)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((80 + (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)
    else:
        pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((80 + (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)

    if ((90 + 2 * (WIN_WIDTH - 160) // 4) <= mouse_pos[0] <= (90 + 3 * (WIN_WIDTH - 160) // 4)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((90 + 2 * (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)
    else:
        pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((90 + 2 * (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)

    if ((100 + 3 * (WIN_WIDTH - 160 ) // 4) <= mouse_pos[0] <= (100 + 4 * (WIN_WIDTH - 160) // 4)) and (5 <= mouse_pos[1] <= 40):
        pygame.draw.rect(screen, COLOURS["BUTTON_LIGHT"], ((100 + 3 * (WIN_WIDTH - 160) // 4, 5 ), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)
    else:
        pygame.draw.rect(screen, COLOURS["BUTTON_NORMAL"], ((100 + 3 * (WIN_WIDTH - 160) // 4, 5), ((WIN_WIDTH - 160) // 4, 40)), border_radius=10)

    # Adding labels to buttons
    button_height = 12
    a_star_text = buttonFont.render('A*', True, COLOURS["TEXT"])
    a_star_width = (140 + (WIN_WIDTH - 160) // 4) // 2

    bfs_text = buttonFont.render('BFS', True, COLOURS["TEXT"])
    bfs_width = (160 + 2.8 * (WIN_WIDTH - 160) // 4) // 2

    dfs_text = buttonFont.render('DFS', True, COLOURS["TEXT"])
    dfs_width = (180 + 4.8 * (WIN_WIDTH - 160) // 4) // 2

    dijkstra_text = buttonFont.render('Dijkstra', True, COLOURS["TEXT"])
    dijkstra_width = (200 + 6.6 * (WIN_WIDTH - 160) // 4) // 2

    screen.blit(a_star_text, (a_star_width, button_height))
    screen.blit(bfs_text, (bfs_width, button_height))
    screen.blit(dfs_text, (dfs_width, button_height))
    screen.blit(dijkstra_text, (dijkstra_width, button_height))

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
