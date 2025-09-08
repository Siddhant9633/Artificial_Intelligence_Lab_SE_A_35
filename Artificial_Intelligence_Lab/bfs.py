from collections import deque

def bfs_with_path(maze, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])
    visited = {start}
    parent = {start: None}  # Track predecessor of each visited cell

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct the path by backtracking through parent
            path = []
            cell = end
            while cell is not None:
                path.append(cell)
                cell = parent[cell]
            return list(reversed(path))  # Path from start to end

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            next_cell = (nr, nc)
            if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and
                maze[nr][nc] != '#' and next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    return None  # No path found

# Example maze
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

path = bfs_with_path(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path exists.")

