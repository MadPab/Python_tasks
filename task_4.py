def return_true(unsorted, num):
    for e in range(len(unsorted)):
        for k in range(e + 1, len(unsorted)):
            if unsorted[e] + unsorted[k] == num:
                print(True)
                return True
    print(False)


unsorted = [1, 3, 2, 12, 11]
num = 5

return_true(unsorted, num)

