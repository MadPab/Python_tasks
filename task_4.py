def get_sum_of_numbers(unsorted, num):
    for e in range(len(unsorted)):
        for k in range(e + 1, len(unsorted)):
            if unsorted[e] + unsorted[k] == num:
                print(True)
                return True
    print(False)


unsorted = [1, 3, 2, 12, 11]
num = 5

get_sum_of_numbers(unsorted, num)