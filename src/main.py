import pygame
from src.utils.constants import *
from src.utils.grid import *
from src.algorithms import *
from tkinter import Tk, messagebox

pygame.init()
game_grid = create_grid()
is_start = False
is_end = False

button_surface = pygame.Surface((BUTTON_WIN_WIDTH, BUTTON_WIN_HEIGHT))
game_surface = pygame.Surface((GAME_WIN_WIDTH, GAME_WIN_HEIGHT))
master_screen = pygame.display.set_mode((GAME_WIN_WIDTH, GAME_WIN_HEIGHT + BUTTON_WIN_HEIGHT))

pygame.display.set_caption("Searching algorithms by BakhshiZ")

buttonFont = pygame.font.SysFont('Arial', 20)
mouse_held = False
current_button = None
running_alg = False
current_alg = None

running = True
start_x = None
start_y = None
button_width = BUTTON_WIDTH
button_height = 40
button_y = 5
button_spacing = 10
path = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_start and is_end:
                    if not current_alg:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Error', 'Please select an algorithm to run.')
                        continue

                    # Update neighbors for all grid nodes
                    for row in game_grid:
                        for cell in row:
                            cell.get_neighbours(game_grid)

                    path = None
                    running_alg = True
                    print(f"Running {current_alg} algorithm...")

                    # Call the selected algorithm
                    if current_alg == "BFS":
                        path = bfs.bfs(game_grid, start_x, start_y, game_surface, master_screen)
                    # elif current_alg == "A*":
                    #     path = astar.astar(game_grid, start_x, start_y)
                    # elif current_alg == "DFS":
                    #     path = dfs.dfs(game_grid, start_x, start_y)
                    # elif current_alg == "Dijkstra":
                    #     path = dijkstra.dijkstra(game_grid, start_x, start_y)

                    running_alg = False

                    # Visualize the path
                    if path:
                        for node in path:
                            pygame.draw.rect(
                                game_surface,
                                COLOURS[node.get_state()],
                                (node.x * NODE_SPACING, node.y * NODE_SPACING, NODE_SPACING, NODE_SPACING),
                            )
                            master_screen.blit(game_surface, (0, BUTTON_WIN_HEIGHT))
                            pygame.display.update()
                            pygame.time.delay(50)

            elif event.key == pygame.K_c:
                running_alg = False
                reset_grid_paths(game_grid)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False
            current_button = None

        elif (event.type == pygame.MOUSEMOTION and mouse_held) or event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if mouse_y > BUTTON_WIN_HEIGHT:
                if not mouse_held:
                    mouse_held = True
                    current_button = event.button

                # Calculate grid cell based on mouse position
                curr_node_x = mouse_x // NODE_SPACING
                curr_node_y = (mouse_y - BUTTON_WIN_HEIGHT) // NODE_SPACING

                if 0 <= curr_node_x < PLAYABLE_ROWS and 0 <= curr_node_y < PLAYABLE_COLUMNS:
                    curr_node = game_grid[curr_node_x][curr_node_y]

                    if current_button == 1:  # Left-click held
                        if curr_node.colour == COLOURS["NEUTRAL"]:
                            if not is_start:
                                curr_node.set_state("START")
                                start_x, start_y = curr_node.x, curr_node.y
                                is_start = True
                            elif not is_end:
                                curr_node.set_state("END")
                                is_end = True
                            else:
                                curr_node.set_state("BARRIER")

                    elif current_button == 3:  # Right-click held
                        if curr_node.colour != COLOURS["NEUTRAL"]:
                            if curr_node.get_state() == "START":
                                is_start = False
                            elif curr_node.get_state() == "END":
                                is_end = False
                            curr_node.reset_node()
            else:
                if is_start and is_end and not running_alg:
                    button_num = mouse_x // button_width

                    if button_num == 0:
                        current_alg = "A*"
                    elif button_num == 1:
                        current_alg = "BFS"
                    elif button_num == 2:
                        current_alg = "DFS"
                    elif button_num == 3:
                        current_alg = "Dijkstra"

    # Render Buttons
    button_surface.fill(COLOURS["BGCOLOUR"])
    mouse_pos = pygame.mouse.get_pos()
    for i in range(4):
        button_x = 70 + i * (button_spacing + button_width)
        rect = pygame.Rect(button_x, button_y, button_width, button_height)

        # Check if mouse is hovering over the button
        color = COLOURS["BUTTON_LIGHT"] if rect.collidepoint(mouse_pos) else COLOURS["BUTTON_NORMAL"]

        pygame.draw.rect(button_surface, color, rect, border_radius=10)
        text = buttonFont.render(["A*", "BFS", "DFS", "Dijkstra"][i], True, COLOURS["TEXT"])
        text_rect = text.get_rect(center=rect.center)
        button_surface.blit(text, text_rect)

    # Render Grid
    for row in game_grid:
        for cell in row:
            pygame.draw.rect(
                game_surface,
                cell.colour,
                ((cell.x * NODE_SPACING, cell.y * NODE_SPACING), (NODE_SPACING, NODE_SPACING)),
            )

    for i in range(PLAYABLE_ROWS):
        pygame.draw.line(game_surface, COLOURS["GRIDLINES"], (i * NODE_SPACING, 0), (i * NODE_SPACING, GAME_WIN_WIDTH))
    for j in range(PLAYABLE_COLUMNS):
        pygame.draw.line(game_surface, COLOURS["GRIDLINES"], (0, j * NODE_SPACING), (GAME_WIN_WIDTH, j * NODE_SPACING))

    master_screen.blit(button_surface, (0, 0))
    master_screen.blit(game_surface, (0, BUTTON_WIN_HEIGHT))
    pygame.display.update()

pygame.quit()
