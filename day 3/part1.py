with open("input.txt") as file:
    power_banks = [line.strip() for line in file]

    def get_max_joltage(power_bank) -> int:
        batteries = [0, 0]
        for i in range(len(power_bank) - 1):
            battery = int(power_bank[i])
            if battery > batteries[0]:
                batteries[0] = battery
                batteries[1] = int(power_bank[i + 1])
            elif battery > batteries[1]:
                batteries[1] = battery
        
        batteries[1] = max(batteries[1], int(power_bank[-1]))
        return batteries[0] * 10 + batteries[1]

    max_powerbank_joltages = [get_max_joltage(power_bank) for power_bank in power_banks]
    result = sum(max_powerbank_joltages)
    print(f"Answer: {result}")