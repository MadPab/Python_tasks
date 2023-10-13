def true_or_false(number):
    sum_even = 0
    sum_odd = 0
    n1 = number[::2]
    n2 = number[1::2]

    for e in range(len(number)):
        d = int(number[e])
        if e % 2 == 0:
            sum_even += d
        else:
            sum_odd += d

    if (sum_even == sum_odd) or (n1 == n2):
        print(True)
    else:
        print(False)


number = str(input())

true_or_false(number)