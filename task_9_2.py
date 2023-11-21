def get_binary(dec, base):
    result = ''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if dec == 0:
        return '0'

    while dec > 0:
        num = dec % base
        result = digits[num] + result
        dec //= base
    return result


dec = int(input('Введите число для перевода в двоичный код: '))
base = int(input('Введите основание системы в которую хотите перевести: '))
binary_num = get_binary(dec, base)
print(binary_num)