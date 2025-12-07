with open("input.txt") as file:
    grid = [list(line) for line in file]
    paths = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid) - 1):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                paths[i][j] = 1

            if grid[i][j] == 'S' or grid[i][j] == '|':
                if grid[i + 1][j] == '^':
                    grid[i + 1][j - 1] = '|'
                    grid[i + 1][j + 1] = '|'
                    paths[i + 1][j - 1] = paths[i][j] + paths[i + 1][j - 1]
                    paths[i + 1][j + 1] = paths[i][j] + paths[i + 1][j + 1]
                else:
                    grid[i + 1][j] = '|'
                    paths[i + 1][j] = paths[i][j] + paths[i + 1][j]
    
    answer = 0
    for j in range(len(paths[-1])):
        answer += paths[-1][j]
    
    print(f"Answer: {answer}")