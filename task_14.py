from num2words import num2words


def get_number_to_words(number):
    if 0 <= number <= 1000000000:
        return num2words(number, lang='ru').capitalize()
    else:
        return "Число вне диапазона от 0 до 1 миллиарда"


input_number = 134432145
result = get_number_to_words(input_number)
print(result)