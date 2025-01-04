from ..utils.grid import *
from ..utils.constants import COLOURS

def bfs(grid: List[List["Node"]], start_x, start_y):
    visited = []
    queue = [grid[start_x][start_y]]

    while len(queue) != 0:
        if queue[0].colour == COLOURS["END"]:
            path = []
            current_node = queue[0]
            while current_node.get_parent() is not None:
                path.append(current_node)
                current_node = current_node.get_parent()
            path.append(current_node)
            path = path.reverse()
            return path

        visited.append(queue[0])
        for neighbour in queue[0].get_neighbours():
            queue.append(neighbour)
        queue.pop(0)

    return None