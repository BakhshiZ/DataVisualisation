from typing import List
from src.utils.constants import COLOURS, PLAYABLE_ROWS, PLAYABLE_COLUMNS, STATES


class Node:
    def __init__(self, x: int, y: int) -> None:
        self.colour: str = COLOURS["NEUTRAL"]
        self.neighbours: List["Node"] = []
        self.x = x
        self.y = y
        self.parent = None

    def set_state(self, state: str) -> None:
        self.colour = COLOURS[state]

    def get_state(self) -> str:
        return STATES[self.colour]

    def get_neighbours(self, grid) -> List['Node']:
        if not self.neighbours:
            neighbours = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny].colour != COLOURS["BARRIER"]:
                    neighbours.append(grid[nx][ny])
                    self.neighbours.append(Node(nx, ny))
            return neighbours
        else:
            return self.neighbours

    def set_parent(self, parent: 'Node') -> None:
        self.parent = parent

    def get_parent(self) -> 'Node':
        return self.parent

    def reset_node(self):
        self.colour = COLOURS["NEUTRAL"]


def create_grid() -> List[List["Node"]]:
    grid: List[List["Node"]] = []
    for i in range(PLAYABLE_ROWS):
        grid.append([])
        for j in range(PLAYABLE_COLUMNS):
            grid[i].append(Node(i, j))
    return grid


def get_start(grid):
    for i in range(PLAYABLE_ROWS):
        for j in range(PLAYABLE_COLUMNS):
            if grid[i][j].colour == COLOURS["START"]:
                return i, j


def reset_grid_paths(grid):
    for row in grid:
        for node in row:
            if node.colour != COLOURS["NEUTRAL"]:
                node.reset_node()
