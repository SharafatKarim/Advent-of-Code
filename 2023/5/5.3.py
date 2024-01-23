with open("5/test_copy.txt", "r") as file:
    main_string = "".join(file)

main_array = main_string.split('\n')

mappings = {}
destinations = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
                "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

for destination in destinations:
    location = main_array.index(f"{destination} map:")
    try:
        next_location = main_array.index("", location)
    except ValueError:
        next_location = len(main_array)
    mappings[destination] = main_array[location + 1: next_location]


def process_data(second, diff, actual):
    return second <= actual < second + diff


def destination(actual, array):
    for entry in array:
        values = entry.split(' ')
        if process_data(int(values[1]), int(values[2]), actual):
            return int(int(values[0]) + (actual - int(values[1])))
    return actual


values = {}
seed_list = [int(seed) for seed in main_array[0].split(' ')[1::2]]

number = 0
min_value = float('inf')

for i in range(0, len(seed_list), 2):
    number += 1
    print(number)
    for j in range(seed_list[i], seed_list[i] + seed_list[i + 1]):
        for destination_key in destinations:
            mappings_array = mappings[destination_key]
            actual_value = destination(j, mappings_array)
            values[j] = actual_value
            if actual_value < min_value:
                min_value = actual_value

print(min_value)
