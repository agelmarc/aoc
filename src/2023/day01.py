from aocd import get_data

a = get_data(
    "53616c7465645f5ff3a1b58eb769871ce3f421d570f24a194c2f4f441946869b8fe3bf328c8cf44c5939f9d22dee924a2c61e2f41f2908e46dd8fe995763ffaa",
    1,
    2023,
)


summe = 0

for line in a.splitlines():
    numbers = []
    for i, char in enumerate(line):
        if char.isnumeric():
            numbers.append(char)

        for i, num_str in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if line[i:].startswith(num_str):
                numbers.append(str(i))
    print(line, numbers)
    summe += int(numbers[0] + numbers[-1])

print(summe)
