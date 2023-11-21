





def get_money(amount, withdrawal_type, available_denominations):
    if amount % 100 != 0:
        raise BadFormatException("Сумма должна быть кратной 100")

    denominations = [int(denom) for denom in available_denominations.keys()]
    result = []

    for denomination in denominations:
        if denomination not in [100, 200, 500, 1000, 2000, 5000]:
            raise BadFormatException(f"Недопустимый номинал {denomination}")

        count_requested = amount // denomination
        count_available = available_denominations.get(str(denomination), 0)

        count_to_withdraw = min(count_requested, count_available)

        if count_to_withdraw > 0:
            if withdrawal_type == "с разменом":
                result.extend([denomination] * count_to_withdraw)
            else:
                result.append([denomination, count_to_withdraw])
            amount -= count_to_withdraw * denomination

    if amount != 0:
        raise BadSumException("Невозможно выдать запрошенную сумму")

    return result


withdrawal_amount = 9800
withdrawal_type = "крупными"
available_denominations = {"100": 3, "500": 3, "2000": 1}

class BadFormatException(Exception):
    pass

class BadSumException(Exception):
    pass

try:
    result = get_money(withdrawal_amount, withdrawal_type, available_denominations)
    print(result)
except BadFormatException as _format:
    print(f"{_format}")
except BadSumException as _sum:
    print(f"{_sum}")