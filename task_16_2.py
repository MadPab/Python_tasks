def check_array(array1: list, array2: list):
    set_array2 = set(array2)

    for digit in set_array2:
        if digit not in set(array1):
            return False
    return True


array1 = [1, 2, 3, 4, 5, 6, 2, 65, 7, 153535, 142124514, 563]
array2 = [2, 4, 6, 7, 153535]
result = check_array(array1, array2)
print(result)