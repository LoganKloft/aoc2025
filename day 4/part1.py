with open("input.txt") as file:
    def is_roll(i, j, grid):
        return grid[i][j] == '@'
    
    def passes_adjacent_check(i, j, grid):
        num_rolls_adjacent = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for direction in directions:
            i_adjusted = i + direction[0]
            j_adjusted = j + direction[1]
            if i_adjusted < 0 or i_adjusted >= len(grid):
                continue
            if j_adjusted < 0 or j_adjusted >= len(grid[0]):
                continue
            if grid[i_adjusted][j_adjusted] == '@':
                num_rolls_adjacent += 1
        return num_rolls_adjacent < 4

    grid = [line.strip() for line in file]
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_roll(i, j, grid) and passes_adjacent_check(i, j, grid):
                result += 1
    
    print(f"Answer: {result}")