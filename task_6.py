def true_or_false(number):
    n1 = number // 10
    n2 = number % 10
    if (n1 == n2) or (n1 + n2 == 10):
        print(True)
    else:
        print(False)


number = int(input())

true_or_false(number)