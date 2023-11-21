from num2words import num2words


def get_number_to_words(number):
    if 0 <= number <= 1000000000:
        result = num2words(number, lang='ru').capitalize()
        last_dig = number % 10

        if last_dig == 1:
            return f"{result} котик"
        elif 2 <= last_dig <= 4:
            return f"{result} котика"
        else:
            return f"{result} котиков"

    else:
        return "Число вне диапазона от 0 до 1 миллиарда"


input_number = 134432141
result = get_number_to_words(input_number)
print(result)