with open("input.txt") as file:
    power_banks = [line.strip() for line in file]

    def get_max_joltage(power_bank) -> int:
        power_bank = [int(battery) for battery in power_bank]
        num_batteries = 12
        batteries = []
        left_idx = 0
        right_idx = len(power_bank) - num_batteries

        for _ in range(num_batteries):
            max_battery = 0
            for j in range(left_idx, right_idx + 1):
                if power_bank[j] > max_battery:
                    max_battery = power_bank[j]
                    left_idx = j + 1
            right_idx += 1
            batteries.append(max_battery)
        
        joltage = 0
        for i in range(len(batteries)):
            joltage += (10 ** (len(batteries) - i - 1)) * batteries[i]
        return joltage

    max_powerbank_joltages = [get_max_joltage(power_bank) for power_bank in power_banks]
    result = sum(max_powerbank_joltages)
    print(f"Answer: {result}")