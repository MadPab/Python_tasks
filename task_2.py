def text_analyze(text, max_symb):
    count_symb = len(text) # длиная теста
    count_symb_no_space = len(text.replace(' ', '')) # Убираем пробелы
    if count_symb > 0:
        print(f"Количество символов в тексте: {count_symb}")
        print(f"Количество символов в тексте без учета пробелов: {count_symb_no_space}")
    if count_symb % 2 == 0:
        print("Количество символов в тексте четное")
    else:
        print("Количество символов в тексте нечетное")
    if max_symb < count_symb:
        s = count_symb - max_symb
        print(f"Длина текста превышает длину {s} символов")
    print("")


text = input("Введите текст: ") # Текст
max_symb = int(input("Введите число: ")) # Максимальная длина

text_analyze(text, max_symb)