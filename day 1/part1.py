with open("input.txt") as file:
    dial = 50
    dial_max_value = 100
    result = 0

    for line in file:
        line = line.strip()
        rotation = int(line[1:]) % dial_max_value

        dial += dial_max_value
        if line[0] == 'L':
            dial -= rotation
        else:
            dial += rotation
        
        dial = dial % dial_max_value
        if dial == 0:
            result += 1
        
    print(f"Answer: {result}")
