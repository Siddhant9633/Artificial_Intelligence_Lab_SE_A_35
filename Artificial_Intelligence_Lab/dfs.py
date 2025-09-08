def dfs_print_path(maze, start, end):
    stack = [start]
    visited = {start}
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == end:
            # Reconstruct path from end to start using parent links
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()

            print(True)
            print("Path:", path)
            return True, path

        x, y = current
        # Explore neighbors: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            nx, ny = neighbor
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                    maze[nx][ny] == 0 and neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    print(False)
    return False, None

# Sample usage
if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    exists, path = dfs_print_path(maze, start, end)

