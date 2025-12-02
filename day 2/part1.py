with open("input.txt") as file:
    id_line = file.readline().strip()
    id_range_list = id_line.split(",")
    id_range_list = [(int(id_range.split("-")[0]), int(id_range.split("-")[1])) for id_range in id_range_list]

    def get_num_digits(n):
        digits = 0
        while n > 0:
            n //= 10
            digits += 1
        return digits

    def is_valid_id(id):
        digits = get_num_digits(id)
        if digits % 2 == 1:
            return False
        
        id_str = str(id)
        return id_str[0 : digits // 2] == id_str[digits // 2 : ]


    result = 0
    for id_range in id_range_list:
        for id in range(id_range[0], id_range[1] + 1):
            if is_valid_id(id):
                result += id

    print(f"Answer: {result}")