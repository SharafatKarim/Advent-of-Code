from io import TextIOWrapper

file: TextIOWrapper = open("2/test_copy.txt", "r")
sum = 0
for lines in file:
    line_segmants: list[str] = lines.split(':')
    game_number = line_segmants[0].split(' ')[1]
    # print(line_segmants)

    max_red = 0
    max_green = 0
    max_blue = 0
    
    blocks = line_segmants[1].split(';')
    # print(blocks)
    for block in blocks:
        block_segmants: list[str] = block.split(',')
        # print(block_segmants)
        for block_segmant in block_segmants:    
            # print(block_segmant)
            if ("red" in block_segmant):
                numbers: list[str] = block_segmant.split(' ')
                # print(numbers[1])
                if (int(numbers[1]) > max_red):
                    max_red = int(numbers[1])
            if ("green" in block_segmant):
                numbers = block_segmant.split(' ')
                # print(numbers[1])
                if (int(numbers[1]) > max_green):
                    max_green = int(numbers[1])
            if ("blue" in block_segmant):
                numbers = block_segmant.split(' ')
                # print(numbers[1])
                if (int(numbers[1]) > max_blue):
                    max_blue = int(numbers[1])
    print(max_red * max_green * max_blue)
    sum += max_red * max_green * max_blue

print("Sum: ")
print(sum)