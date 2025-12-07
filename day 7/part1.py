with open("input.txt") as file:
    grid = [list(line) for line in file]
    for i in range(len(grid) - 1):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S' or grid[i][j] == '|':
                if grid[i + 1][j] == '^':
                    grid[i + 1][j - 1] = '|'
                    grid[i + 1][j + 1] = '|'
                else:
                    grid[i + 1][j] = '|'
    
    answer = 0
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^' and grid[i - 1][j] == '|':
                answer += 1
    
    print(f"Answer: {answer}")