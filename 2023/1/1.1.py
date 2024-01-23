from io import TextIOWrapper

file: TextIOWrapper = open("test_copy.txt", "r")
sum = 0
for lines in file:
    str = ""
    for i in range(len(lines)):
        if (lines[i] >= '0' and lines[i] <= '9'):
            str += lines[i]
        if (lines[i:i+3]=="one"):
            str += '1'
            i += 3
        elif (lines[i:i+3]=="two"):
            str += '2'
        elif (lines[i:i+5]=="three"):
            str += '3'
        elif (lines[i:i+4]=="four"):
            str += '4'
        elif (lines[i:i+4]=="five"):
            str += '5'
        elif (lines[i:i+3]=="six"):
            str += '6'
        elif (lines[i:i+5]=="seven"):
            str += '7'
        elif (lines[i:i+5]=="eight"):
            str += '8'
        elif (lines[i:i+4]=="nine"):
            str += '9'
    # print(str)
    sum += int(str[0]+str[-1])
print(sum)