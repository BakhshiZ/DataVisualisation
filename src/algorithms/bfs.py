from src.utils.constants import *
import pygame

def bfs(grid, start_x, start_y, game_surface, master_screen):
    start_node = grid[start_x][start_y]
    queue = [start_node]
    visited = set()

    while queue:
        current_node = queue.pop(0)

        # If the current node is the "END" node, construct the path and exit
        if current_node.get_state() == "END":
            path = []
            while current_node:
                current_node.set_state("PATH")  # Set the path state for visualization
                path.append(current_node)
                current_node = current_node.get_parent()
            path.reverse()  # Reverse the path to get it from start to end
            return path

        # Mark the current node as visited, but skip marking "END"
        if current_node.get_state() != "START" and current_node.get_state() != "END":
            current_node.set_state("VISITED")
            visited.add(current_node)

        # Render the current state
        pygame.draw.rect(
            game_surface,
            COLOURS[current_node.get_state()],
            (current_node.x * NODE_SPACING, current_node.y * NODE_SPACING, NODE_SPACING, NODE_SPACING),
        )
        master_screen.blit(game_surface, (0, BUTTON_WIN_HEIGHT))
        pygame.display.update()
        pygame.time.delay(50)

        # Add neighbors to the queue if they are not visited or barriers
        for neighbor in current_node.get_neighbours(grid):
            if neighbor.get_state() == "END":
                neighbor.set_parent(current_node)  # Link the end node to its parent
                queue.append(neighbor)  # Add end node to process path reconstruction
                break
            elif neighbor.get_state() == "START":
                continue
            if neighbor not in visited and neighbor not in queue and neighbor.get_state() != "BARRIER":
                neighbor.set_parent(current_node)
                neighbor.set_state("TO_BE_VISITED")
                queue.append(neighbor)

                # Render "TO_BE_VISITED" state
                pygame.draw.rect(
                    game_surface,
                    COLOURS[neighbor.get_state()],
                    (neighbor.x * NODE_SPACING, neighbor.y * NODE_SPACING, NODE_SPACING, NODE_SPACING),
                )
                master_screen.blit(game_surface, (0, BUTTON_WIN_HEIGHT))
                pygame.display.update()
                pygame.time.delay(50)

    # If no path is found, return None
    return None
