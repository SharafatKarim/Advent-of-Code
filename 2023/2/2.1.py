from io import TextIOWrapper

file: TextIOWrapper = open("2/test_copy.txt", "r")
sum = 0
for lines in file:
    is_valid = True
    line_segmants: list[str] = lines.split(':')
    game_number = line_segmants[0].split(' ')[1]
    # print(line_segmants)

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
                if (int(numbers[1]) > 12):
                    is_valid = False
                    break
            if ("green" in block_segmant):
                numbers = block_segmant.split(' ')
                # print(numbers[1])
                if (int(numbers[1]) > 13):
                    is_valid = False
                    break
            if ("blue" in block_segmant):
                numbers = block_segmant.split(' ')
                # print(numbers[1])
                if (int(numbers[1]) > 14):
                    is_valid = False
                    break
    if (is_valid):
        print(game_number)
        sum += int(game_number)

print("Sum: ")
print(sum)