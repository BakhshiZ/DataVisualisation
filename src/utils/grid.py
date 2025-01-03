"""
* grid is 2d array of states, has start coord, end coord, stores states
*
"""
from typing import List
from constants import COLOURS, PLAYABLE_ROWS, PLAYABLE_COLUMNS, STATES

class Node:
    def __init__(self, x: int, y: int) -> None:
        self.colour: str = COLOURS["NEUTRAL"]
        self.neighbours: List['Node'] = []
        self.x: int = x
        self.y: int = y

    def __lt__(self, other: 'Node') -> bool:
        return False

    def set_state(self, state: str) -> None:
        self.colour = COLOURS[state]

    def get_state(self) -> str:
        return STATES[self.colour]

    def set_neighbours(self, neighbours: List['Node']) -> None:
        self.neighbours = neighbours

    def get_neighbours(self) -> List['Node']:
        return self.neighbours


def create_grid() -> List[List[Node]]:
    grid: List[List[Node]] = []
    for i in range(PLAYABLE_ROWS):
        grid.append([])
        for j in range(PLAYABLE_COLUMNS):
            grid[i].append(Node(i, j))
    return grid