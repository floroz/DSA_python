from collections import deque


def shortest_path_bidirectional(grid, start, end) -> int:
    """
    Find the shortest path between two points in a grid.
    :param grid: The grid to traverse.
    :param start: The starting point.
    :param end: The ending point.
    :return: The shortest path between the start and end points.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    visited_start = set([start])
    visited_end = set([end])

    queue_start = deque([start])
    queue_end = deque([end])

    path_start = {start: 0}
    path_end = {end: 0}

    def neighbors(node):
        # Only allow up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        (x, y) = node
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1:
                yield (nx, ny)

    while queue_start and queue_end:
        if queue_start:
            cell_start = queue_start.popleft()
            # if the current node is in the visited_end set, we have found a path
            if cell_start in visited_end:
                return path_start[cell_start] + path_end[cell_start]
            for neighbor in neighbors(cell_start):
                if neighbor not in visited_start:
                    queue_start.append(neighbor)
                    visited_start.add(neighbor)
                    path_start[neighbor] = path_start[cell_start] + 1

        if queue_end:
            cell_end = queue_end.popleft()
            # if the current node is in the visited_start set, we have found a path
            if cell_end in visited_start:
                return path_start[cell_end] + path_end[cell_end]
            for neighbor in neighbors(cell_end):
                if neighbor not in visited_end:
                    queue_end.append(neighbor)
                    visited_end.add(neighbor)
                    path_end[neighbor] = path_end[cell_end] + 1

    return -1  # No path found


def test_4_x_4():
    """
    Test case for a 4x4 grid with a path between the start and end points.
    """
    four_by_four = (
        [2, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2])

    assert shortest_path_bidirectional(four_by_four, (0, 0), (3, 3)) == 6


def test_4_x_4_no_path():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    result = shortest_path_bidirectional(grid, start, end)
    assert result == 6


def test_6_x_6_no_path():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (5, 5)
    result = shortest_path_bidirectional(grid, start, end)
    assert result == 10


def test_6_x_6():
    """
    Test case for a 6x6 grid with a path between the start and end points.
    """
    six_by_six = [
        [0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0]
    ]

    start = (1, 1)
    end = (5, 2)
    result = shortest_path_bidirectional(six_by_six, start, end)
    assert result == 7


def test_next_to_each_other():
    """
    Test case for a 5x5 grid with the start and end points next to each other.
    """
    by_each_other = (
        [0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    )

    assert shortest_path_bidirectional(by_each_other, (1, 1), (2, 1), ) == 1


def test_empty_grid():
    """
    Test case for an empty grid.
    """
    grid = []
    start = (0, 0)
    end = (0, 0)
    result = shortest_path_bidirectional(grid, start, end)
    assert result == 0


def test_large_grid():
    """
    Test case for a large grid (10x10) with a path between the start and end points.
    """
    large_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start = (1, 1)
    end = (8, 8)
    result = shortest_path_bidirectional(large_grid, start, end)
    assert result == 18


def test_no_obstacles():
    """
    Test case for a 3x3 grid with no obstacles.
    """
    no_obstacles = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    start = (0, 0)
    end = (2, 2)
    result = shortest_path_bidirectional(no_obstacles, start, end)
    assert result == 4
