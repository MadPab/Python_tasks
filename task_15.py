def get_money(amount, withdrawal_type):
    denominations = [5000, 2000, 1000, 500, 200, 100]
    result = []

    for denomination in denominations:
        count = amount // denomination
        if count > 0:
            if withdrawal_type == "с разменом":
                result.extend([denomination] * count)
            else:
                result.append([denomination, count])
            amount %= denomination

    return result

withdrawal_amount = 4500
withdrawal_type = "с разменом"
result = get_money(withdrawal_amount, withdrawal_type)
print(result)
