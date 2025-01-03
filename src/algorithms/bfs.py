"""
visited, queue = empty
queue = start
visited = start

pop start
queue the neigbours

visit neighbour one, add to visited and pop it from queue
queue its neighbours

visit neighbour two, add to visited and pop it from queue
queue its neighbours

visit neighbour one first neighbour, add to visited amd pop it from queue
queue its neighbours

repeat until no more nodes or at end
"""

def bfs(grid):
    visited = []
    queue = []