def text_analyze(n1, n2, text):
    if n2 != 0:
        print(n2)
    if q in range(text) == ' ':
        print(len(q))
    if n2 % 2 == 0:
        print("Количество символов в тексте четное")
    else:
        print("Количество символов в тексте нечетное")
    if n1 > n2:
        print(f"Длина текста превышает длину {n1} символов")


text = input("Введите текст: ")
n1 = int(input("Введите число: "))
n2 = len(text)
q = []

text_analyze(n1, n2, text)