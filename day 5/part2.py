with open("input.txt") as file:
    fresh_ranges = []

    for line in file:
        line = line.strip()
        if line == '':
            break
        fresh_range = line.split('-')
        fresh_range = [int(id) for id in fresh_range]
        fresh_ranges.append(fresh_range)
    
    def merge_ranges(ranges):
        ranges.sort(key = lambda range: range[0])
        merged_ranges = []

        for range in ranges:
            if len(merged_ranges) == 0 or range[0] > merged_ranges[-1][1]:
                merged_ranges.append(range)
            else:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], range[1])
        
        return merged_ranges  

    merged_fresh_ranges = merge_ranges(fresh_ranges)
    
    result = 0
    for range in merged_fresh_ranges:
        result += range[1] - range[0] + 1
    
    print(f"Answer: {result}")