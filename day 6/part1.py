with open("input.txt") as file:
    equations = [equation.strip().split() for equation in file]
    puzzle_result = 0
    for i in range(len(equations[-1])):
        operator = equations[-1][i]
        function_result = int(equations[0][i])
        for j in range(1, len(equations) - 1):
            if operator == '+':
                function_result += int(equations[j][i])
            if operator == '*':
                function_result *= int(equations[j][i])
        puzzle_result += function_result
    print(f"Answer: {puzzle_result}")