file = open("5/test.txt", "r")
sum = 0
main_string = ""

i = 0
for lines in file:
    for line in lines:
        main_string += line

file.close()

main_array = main_string.split('\n')

# print(main_array[0].split(' ')[1:])

seed_to_soil_location = 0
soil_to_fertilizer_location = 0
fertilizer_to_water_location = 0
water_to_light_location = 0
light_to_temperature_location = 0
temperature_to_humidity_location = 0
humidity_to_location_location = 0

for line in main_array:
    if line == "seed-to-soil map:":
        seed_to_soil_location = main_array.index(line)
    elif line == "soil-to-fertilizer map:":
        soil_to_fertilizer_location = main_array.index(line)
    elif line == "fertilizer-to-water map:":
        fertilizer_to_water_location = main_array.index(line)
    elif line == "water-to-light map:":
        water_to_light_location = main_array.index(line)
    elif line == "light-to-temperature map:":
        light_to_temperature_location = main_array.index(line)
    elif line == "temperature-to-humidity map:":
        temperature_to_humidity_location = main_array.index(line)
    elif line == "humidity-to-location map:":
        humidity_to_location_location = main_array.index(line)

# print(humidity_to_location_location)

seed_to_soil = main_array[seed_to_soil_location +
                          1:soil_to_fertilizer_location-1]
# print(seed_to_soil)
soil_to_fertilizer = main_array[soil_to_fertilizer_location +
                                1:fertilizer_to_water_location-1]
fertilizer_to_water = main_array[fertilizer_to_water_location +
                                 1:water_to_light_location-1]
water_to_light = main_array[water_to_light_location +
                            1:light_to_temperature_location-1]
light_to_temperature = main_array[light_to_temperature_location +
                                  1:temperature_to_humidity_location-1]
temperature_to_humidity = main_array[temperature_to_humidity_location +
                                     1:humidity_to_location_location-1]
humidity_to_location = main_array[humidity_to_location_location + 1:]

# print(humidity_to_location)


def process_data(second, diff, actual):
    if second <= actual and second + diff > actual:
        return True
    else:
        return False


def destination_seed_to_soil(actual):
    for every_seed_to_soil in seed_to_soil:
        every_seed_to_soil = every_seed_to_soil.split(' ')
        if process_data(int(every_seed_to_soil[1]), int(every_seed_to_soil[2]), actual):
            return int(int(every_seed_to_soil[0])+(actual-int(every_seed_to_soil[1])))
    return actual


def destination_soil_to_fertilizer(actual):
    for every_soil_to_fertilizer in soil_to_fertilizer:
        every_soil_to_fertilizer = every_soil_to_fertilizer.split(' ')
        if process_data(int(every_soil_to_fertilizer[1]), int(every_soil_to_fertilizer[2]), actual):
            return int(int(every_soil_to_fertilizer[0])+(actual-int(every_soil_to_fertilizer[1])))
    return actual


def destination_fertilizer_to_water(actual):
    for every_fertilizer_to_water in fertilizer_to_water:
        every_fertilizer_to_water = every_fertilizer_to_water.split(' ')
        if process_data(int(every_fertilizer_to_water[1]), int(every_fertilizer_to_water[2]), actual):
            return int(int(every_fertilizer_to_water[0])+(actual-int(every_fertilizer_to_water[1])))
    return actual


def destination_water_to_light(actual):
    for every_water_to_light in water_to_light:
        every_water_to_light = every_water_to_light.split(' ')
        if process_data(int(every_water_to_light[1]), int(every_water_to_light[2]), actual):
            return int(int(every_water_to_light[0])+(actual-int(every_water_to_light[1])))
    return actual


def destination_light_to_temperature(actual):
    for every_light_to_temperature in light_to_temperature:
        every_light_to_temperature = every_light_to_temperature.split(' ')
        if process_data(int(every_light_to_temperature[1]), int(every_light_to_temperature[2]), actual):
            return int(int(every_light_to_temperature[0])+(actual-int(every_light_to_temperature[1])))
    return actual


def destination_temperature_to_humidity(actual):
    for every_temperature_to_humidity in temperature_to_humidity:
        every_temperature_to_humidity = every_temperature_to_humidity.split(
            ' ')
        if process_data(int(every_temperature_to_humidity[1]), int(every_temperature_to_humidity[2]), actual):
            return int(int(every_temperature_to_humidity[0])+(actual-int(every_temperature_to_humidity[1])))
    return actual


def destination_humidity_to_location(actual):
    for every_humidity_to_location in humidity_to_location:
        every_humidity_to_location = every_humidity_to_location.split(' ')
        if process_data(int(every_humidity_to_location[1]), int(every_humidity_to_location[2]), actual):
            return int(int(every_humidity_to_location[0])+(actual-int(every_humidity_to_location[1])))
    return actual

# print(destination_seed_to_soil(99))
# print(process_data(50, 48, 55))


# ----------------------------------------
seeds = main_array[0].split(' ')[1:]
# print(destination_seed_to_soil(seeds[0]))

# print(destination_humidity_to_location(destination_humidity_to_location(destination_temperature_to_humidity(destination_light_to_temperature(destination_water_to_light(destination_fertilizer_to_water(destination_soil_to_fertilizer(destination_seed_to_soil(int(seeds[0]))))))))))

values = {}
seed_list = []
for seed in seeds:
    seed_list.append(int(seed))

number = 0
min_value = 1000000000000


def max_heavy_lifting(j):
    global min_value
    value = destination_humidity_to_location(destination_humidity_to_location(destination_temperature_to_humidity(destination_light_to_temperature(
        destination_water_to_light(destination_fertilizer_to_water(destination_soil_to_fertilizer(destination_seed_to_soil(int(j)))))))))
    values[j] = value
    if value < min_value:
        min_value = value


for i in range(0, len(seed_list), 2):
    number += 1
    print(number)
    for j in range(seed_list[i], seed_list[i]+seed_list[i+1]):
        # print(j)
        max_heavy_lifting(int(j))
        # value = destination_humidity_to_location(destination_humidity_to_location(destination_temperature_to_humidity(destination_light_to_temperature(
        #     destination_water_to_light(destination_fertilizer_to_water(destination_soil_to_fertilizer(destination_seed_to_soil(int(j)))))))))
        # values[int(j)] = value
        # if value < min_value:
        #     min_value =

        # values.append(destination_humidity_to_location(destination_humidity_to_location(destination_temperature_to_humidity(destination_light_to_temperature(
        # destination_water_to_light(destination_fertilizer_to_water(destination_soil_to_fertilizer(destination_seed_to_soil(int(j))))))))))

# print(seed_list)
# print(min(values))
print(min_value)
