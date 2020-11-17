def binary_number_conversion(num):
    list_conversion = []
    division = 2
    while division != 1:
        divison = int(num/2)
        rest_of_division = num % 2
        list_conversion.append(rest_of_division)
        num = divison
        division = num
    list_conversion = [str(i) for i in list_conversion[::-1]]
    list_conversion.insert(0, str(1))
    binary_number = ""
    for i in list_conversion:
        binary_number = binary_number + i
    return binary_number

numbers_to_convert = []
[numbers_to_convert.append(int(input("Enter a number to convert in binary:"))) for i in range(2)]
arq = open("binary-number.txt", "w")
for number in numbers_to_convert:
    arq.write(binary_number_conversion(number) + "\n")