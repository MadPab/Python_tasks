def get_binary(dec):
    result = ''

    if dec == 0:
        return '0'

    while dec > 0:
        num = dec % 2
        result = str(num) + result
        dec //= 2
    return result


dec = int(input('Введите число для перевода в двоичный код: '))
binary_num = get_binary(dec)
print(binary_num)