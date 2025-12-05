with open("input.txt") as file:
    fresh_ranges = []
    ingredient_ids = []

    for line in file:
        line = line.strip()
        if line == '':
            break
        fresh_range = line.split('-')
        fresh_range = [int(id) for id in fresh_range]
        fresh_ranges.append(fresh_range)
    
    for line in file:
        line = line.strip()
        ingredient_ids.append(int(line))

    result = 0
    for id in ingredient_ids:
        for fresh_range in fresh_ranges:
            if id >= fresh_range[0] and id <= fresh_range[1]:
                result += 1
                break
    
    print(f"Answer: {result}")