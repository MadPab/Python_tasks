def find_path(grid):
    def grid(x, y, color):
        return 0 <= x < 3 and 0 <= y < 3 and color_match[x][y] == color

    def find_the_way(x, y, visited):
        if x == 2 and y == 2:
            return True
        visited[x][y] = True

    for dx, dy in [(0, 1), (1, 0)]

