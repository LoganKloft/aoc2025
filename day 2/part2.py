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
        id_str = str(id)
        num_digits = 1
        max_digits = get_num_digits(id)
        while num_digits <= max_digits // 2:
            if max_digits % num_digits != 0:
                num_digits += 1
                continue
            valid_id = True
            idx = num_digits
            while idx + num_digits <= max_digits:
                if id_str[0:num_digits] != id_str[idx:idx+num_digits]:
                    valid_id = False
                    break
                idx += num_digits
            if valid_id:
                return True
            num_digits += 1
        return False

    result = 0
    for id_range in id_range_list:
        for id in range(id_range[0], id_range[1] + 1):
            if is_valid_id(id):
                result += id

    print(f"Answer: {result}")