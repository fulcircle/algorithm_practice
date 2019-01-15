# Solves https://www.geeksforgeeks.org/largest-connected-component-on-a-grid/
from collections import defaultdict

input_grid = [
    [1, 4, 4, 4, 4, 3, 3, 1],
    [2, 1, 1, 4, 3, 3, 1, 1],
    [3, 2, 1, 1, 2, 3, 2, 1],
    [3, 3, 2, 1, 2, 2, 2, 2],
    [3, 1, 3, 1, 1, 4, 4, 4],
    [1, 1, 3, 1, 1, 4, 4, 4]
]

def largest_connected_component(grid):

    visited = [[False for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
    max_lengths = [0]*4

    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):

            current_coordinate = (row_idx, col_idx)

            length = grid_bfs(grid, visited, current_coordinate)
            if length > max_lengths[value-1]:
                max_lengths[value-1] = length

    return max_lengths


def grid_bfs(grid, visited, start_coordinate):

    grid_queue = [start_coordinate]
    length = 0


    while len(grid_queue) > 0:
        current_coordinate = grid_queue.pop(0)

        row = current_coordinate[0]
        col = current_coordinate[1]

        if not visited[row][col]:
            length += 1
            visited[row][col] = True

            neighbors = get_same_neighbors(grid, current_coordinate)

            for neighbor in neighbors:
                grid_queue.append(neighbor)

    return length


def get_same_neighbors(grid, current_coordinate):

    row = current_coordinate[0]
    col = current_coordinate[1]
    value = grid[row][col]
    neighbors = []

    if row+1 < len(grid) and grid[row+1][col] == value:
        neighbors.append((row+1, col))
    
    if row-1 >= 0 and grid[row-1][col] == value:
        neighbors.append((row-1, col))

    if col-1 >= 0 and grid[row][col-1] == value:
        neighbors.append((row, col-1))

    if col+1 < len(grid[0]) and grid[row][col+1] == value:
        neighbors.append((row, col+1))

    return neighbors


print(largest_connected_component(input_grid))
