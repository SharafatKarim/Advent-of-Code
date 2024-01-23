from io import TextIOWrapper

file: TextIOWrapper = open("4/test.txt", "r")
sum = 0
main_string = ""

i = 0
for lines in file:
    for line in lines:
        main_string += line

file.close()

def write_to_file(main_string, destination):
    file = open(destination, "w")
    file.write(main_string)
    file.close()

main_array = main_string.split('\n')

# print(main_array)

card_array = []
for i in range(201):
    card_array.append(1)

current_index = 0
for card_lines in main_array:
    # print(card_lines)
    card_main_array = card_lines.split(':')
    # print(card_main_array[1])
    card_both_side = card_main_array[1].split('|')
    # print(card_both_side[0].strip().split(' '))
    
    card_left_side = card_both_side[0].strip().split(' ')
    # print(card_left_side)

    card_right_side = card_both_side[1].strip().split(' ')
    # print(card_right_side)

    count_simillar = 0
    for left_side in card_left_side:
        for right_side in card_right_side:
            if (left_side == right_side and left_side != ' ' and left_side != ''):
                count_simillar += 1
    print(count_simillar)

    for i in range(count_simillar):
        card_array[current_index + i + 1] += card_array[current_index]

    current_index += 1

    

    # if (count_simillar > 0):
    #     print(2 ** (count_simillar - 1))
    #     sum += 2 ** (count_simillar - 1)

print(card_array)
for i in range(len(card_array)):
    sum += card_array[i]

print("Sum: ", end='')
print(sum)

# 1 2 4 8 14 1 = 30
