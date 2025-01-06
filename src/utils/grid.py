from typing import List
from src.utils.constants import COLOURS, PLAYABLE_ROWS, PLAYABLE_COLUMNS, STATES

class Node:
    def __init__(self, x: int, y: int) -> None:
        self.colour = COLOURS["NEUTRAL"]
        self.neighbours: List["Node"] = []
        self.x = x
        self.y = y
        self.parent = None

    def set_state(self, state: str) -> None:
        self.colour = COLOURS[state]

    def get_state(self) -> str:
        return STATES[self.colour]

    def get_neighbours(self, grid) -> List['Node']:
        neighbors = []
        if self.y + 1 < PLAYABLE_COLUMNS and grid[self.x][self.y + 1].get_state() != "BARRIER":
            neighbors.append(grid[self.x][self.y + 1])
        if self.x + 1 < PLAYABLE_ROWS and grid[self.x + 1][self.y].get_state() != "BARRIER":
            neighbors.append(grid[self.x + 1][self.y])
        if self.x - 1 >= 0 and grid[self.x - 1][self.y].get_state() != "BARRIER":
            neighbors.append(grid[self.x - 1][self.y])
        if self.y - 1 >= 0 and grid[self.x][self.y - 1].get_state() != "BARRIER":
            neighbors.append(grid[self.x][self.y - 1])
        return neighbors

    def set_parent(self, parent: 'Node') -> None:
        self.parent = parent

    def get_parent(self) -> 'Node':
        return self.parent

    def reset_node(self):
        self.colour = COLOURS["NEUTRAL"]
        self.neighbours = []
        self.parent = None

def create_grid() -> List[List["Node"]]:
    grid: List[List["Node"]] = []
    for i in range(PLAYABLE_ROWS):
        grid.append([])
        for j in range(PLAYABLE_COLUMNS):
            grid[i].append(Node(i, j))
    return grid

def get_start(grid: List[List["Node"]]):
    for row in grid:
        for cell in row:
            if cell.get_state() == "START":
                return cell

def reset_grid_paths(grid):
    for row in grid:
        for node in row:
            if node.get_state() in ["PATH", "VISITED", "TO_BE_VISITED"]:
                node.reset_node()