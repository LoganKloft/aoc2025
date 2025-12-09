with open("input.txt") as file:
    class Junction():
        def __init__(self, line):
            self.location = line.strip().split(',')
            self.location = [int(self.location[0]), int(self.location[1]), int(self.location[2])]

        def distance(self, other):
            return ((self.location[0] - other.location[0]) ** 2 + (self.location[1] - other.location[1]) ** 2 + (self.location[2] - other.location[2]) ** 2) ** 0.5
        
        def __repr__(self):
            return f"{self.location}"
        
        def __eq__(self, other):
            return self.location == other.location
    
    junctions = [Junction(line) for line in file]
    shortest_distances = []
    
    for i in range(len(junctions)):
        junction1 = junctions[i]
        for j in range(i + 1, len(junctions)):
            junction2 = junctions[j]
            shortest_distances.append((junction1.distance(junction2), junction1, junction2))
    
    shortest_distances.sort(key = lambda x : x[0])
    
    circuits = []
    shortest_distance_idx = 0
    while True:
        junction1 = shortest_distances[shortest_distance_idx][1]
        junction2 = shortest_distances[shortest_distance_idx][2]

        if junction1 == junction2:
            shortest_distance_idx += 1
            continue

        saved_circuit1_idx = None
        saved_circuit2_idx = None
        for i in range(len(circuits)):
            if junction1 in circuits[i]:
                saved_circuit1_idx = i
            if junction2 in circuits[i]:
                saved_circuit2_idx = i
        
        if saved_circuit1_idx is None and saved_circuit2_idx is None:
            circuits.append([junction1, junction2])
        elif saved_circuit1_idx == saved_circuit2_idx:
            shortest_distance_idx += 1
            continue
        elif saved_circuit1_idx is None:
            assert(saved_circuit2_idx is not None)
            circuits[saved_circuit2_idx].append(junction1)

            if len(circuits[saved_circuit2_idx]) == len(junctions):
                print(f"Answer: {junction1.location[0] * junction2.location[0]}")
                break
        elif saved_circuit2_idx is None:
            assert(saved_circuit1_idx is not None)
            circuits[saved_circuit1_idx].append(junction2)

            if len(circuits[saved_circuit1_idx]) == len(junctions):
                print(f"Answer: {junction1.location[0] * junction2.location[0]}")
                break
        else:
            circuits[saved_circuit1_idx].extend(circuits[saved_circuit2_idx])
            
            if len(circuits[saved_circuit1_idx]) == len(junctions):
                print(f"Answer: {junction1.location[0] * junction2.location[0]}")
                break
            
            circuits.pop(saved_circuit2_idx)
        
        shortest_distance_idx += 1