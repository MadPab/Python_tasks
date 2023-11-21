def get_true_or_false(array: list):
    return 13 in array and 41 in array


array = [1, 2, 13, 4, 5, 41]

result = get_true_or_false(array)
print(result)





# def get_true_or_false(array: list):
#     num_13 = False
#     num_41 = False
#
#     for i in array:
#         if i == 13:
#             num_13 = True
#         elif i == 41:
#             num_41 = True
#
#     return num_13 and num_41
#
# array = [1, 2, 13, 4, 5, 41]
#
# result = get_true_or_false(array)
# print(result)
