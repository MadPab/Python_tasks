def analyze_text(text, max_symbols):
    count_symbols = len(text)
    count_symbols_no_space = len(text.replace(' ', ''))
    if count_symbols > 0:
        print(f"Количество символов в тексте: {count_symbols}")
        print(f"Количество символов в тексте без учета пробелов: {count_symbols_no_space}")
    if count_symbols % 2 == 0:
        print("Количество символов в тексте четное")
    else:
        print("Количество символов в тексте нечетное")
    if max_symbols < count_symbols:
        s = count_symbols - max_symbols
        print(f"Длина текста превышает длину {s} символов")
    print("")


text = input("Введите текст: ")
max_symbols = int(input("Введите число: "))

analyze_text(text, max_symbols)