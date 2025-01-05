from ..utils.grid import *
from ..utils.constants import COLOURS

def bfs(grid: List[List["Node"]], start_x, start_y):
    start_node = grid[start_x][start_y]
    queue = [start_node]
    visited = set()

    while queue:
        current_node = queue.pop(0)
        current_node.colour = COLOURS["VISITED"]

        if current_node.colour == COLOURS["END"]:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.get_parent()
            path.reverse()
            return path

        visited.add(current_node)

        for neighbour in current_node.get_neighbours(grid):
            if neighbour not in visited:
                neighbour.set_parent(current_node)
                neighbour.colour = COLOURS["TO_BE_VISITED"]
                queue.append(neighbour)

    return None
