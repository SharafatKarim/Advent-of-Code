from io import TextIOWrapper

file: TextIOWrapper = open("test_copy.txt", "r")
sum = 0
for lines in file:
    str = ""
    for i in lines:
        if (i >= '0' and i <= '9'):
            str += i;
    sum += int(str[0]+str[-1]);
print(sum)