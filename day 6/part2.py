with open("input.txt") as file:
    equations = [equation.rstrip('\n') for equation in file]
    result = 0
    operator = '.'
    operands = []
    for i in range(len(equations[0])):
        calculate_equation = True
        for j in range(len(equations)):
            if equations[j][i].isdigit():
                calculate_equation = False
                break
        
        if calculate_equation:
            operands = [int(operand) for operand in operands]
            equation_result = operands[0]
            for operand in operands[1:]:
                if operator == '+':
                    equation_result += operand
                elif operator == '*':
                    equation_result *= operand
            result += equation_result
            operator = '.'
            operands = []
            continue
        
        operand = ''
        for j in range(len(equations)):
            if equations[j][i].isdigit():
                operand = operand + equations[j][i]
            if equations[j][i] == '+' or equations[j][i] == '*':
                operator = equations[j][i]
        operands.append(operand)

    operands = [int(operand) for operand in operands]
    equation_result = operands[0]
    for operand in operands[1:]:
        if operator == '+':
            equation_result += operand
        elif operator == '*':
            equation_result *= operand
    result += equation_result

    print(f"Answer: {result}")