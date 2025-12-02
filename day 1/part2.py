with open("input.txt") as file:
    dial = 50
    dial_max_value = 100
    result = 0

    for line in file:
        line = line.strip()
        rotation = int(line[1:]) % dial_max_value
        result += int(line[1:]) // dial_max_value

        dial += dial_max_value
        if line[0] == 'L':
            dial -= rotation
            if dial <= dial_max_value and dial + rotation > dial_max_value:
                result += 1
        else:
            dial += rotation
            if dial >= 2 * dial_max_value:
                result += 1
        
        dial = dial % dial_max_value
        
    print(f"Answer: {result}")
