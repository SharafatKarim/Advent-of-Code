from io import TextIOWrapper

file: TextIOWrapper = open("3/test_copy.txt", "r")
sum = 0

main_string = ""

i = 0
for lines in file:
    # print(lines)

    # two_d_array.append(lines.split(' '))
    for line in lines:
        main_string += line

file.close()

main_array = main_string.split('\n')
# print(main_array[0][1])


def is_digit(character: str) -> bool:
    if (character >= '0' and character <= '9'):
        return True
    else:
        return False


def special_char_check(character: str) -> bool:
    if (character == '*'):
        return True
    else:
        return False


MarkedPart = []


def mark_around(x: int, y: int):
    MarkedPart.append([x-1, y-1])
    MarkedPart.append([x-1, y])
    MarkedPart.append([x-1, y+1])
    MarkedPart.append([x, y-1])
    MarkedPart.append([x, y])
    MarkedPart.append([x, y+1])
    MarkedPart.append([x+1, y-1])
    MarkedPart.append([x+1, y])
    MarkedPart.append([x+1, y+1])


def exist_inside(x: int, y: int) -> bool:
    for i in range(0, len(MarkedPart)):
        if (MarkedPart[i] == [x, y]):
            return True
    return False


def inner_exist_inside():
    ModifiedPart = []
    for i in range(0, len(main_array)):
        is_valid = False
        full_num = ""
        for j in range(0, len(main_array[i])):
            # print(main_array[i][j], end="")
            if (is_digit(main_array[i][j])):
                # print(main_array[i][j], end="")
                if (exist_inside(i, j) and is_digit(main_array[i][j])):
                    is_valid = True
                full_num += main_array[i][j]
            if (((not is_digit(main_array[i][j])) or (j == len(main_array[0])-1))):
                if (is_valid):
                    # print(full_num)
                    ModifiedPart.append(full_num)
                full_num = ""
                is_valid = False
    # print(ModifiedPart)
    return ModifiedPart


for i in range(0, len(main_array)):
    for j in range(0, len(main_array[i])):
        # print(main_array[i][j], end="")
        if (special_char_check(main_array[i][j])):
            # print(main_array[i][j], end="")
            MarkedPart.clear()
            mark_around(i, j)
            # print(MarkedPart)
            Modified = inner_exist_inside()
            if (len(Modified) == 2):
                sum += int(Modified[0]) * int(Modified[1])

print("Sum: ")
print(sum)