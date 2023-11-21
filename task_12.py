Функция получает на вход строку, максимальную длину строки и строку, которая добавится в конец измененной строки.
Если длина строки не длинее максимального значения maxlen, то вернется исходная строка, если же строка превышает
значение maxlen, то строка разбивается на части, используя пробел в качестве разделителя. Далее создается новая строка
пока длина новой строки не станет больше максимальной длины maxlen. В конце к
новой строке добавляется end и строка возвращается


class Helper {
public helper(STRING str, INT maxLen, STRING end) -> STRING {
if (str.length < maxLen) {


return str
}

STRING[]
split = str.split(" ");
STRING
newStr = ""

for (String strPart IN split) {
    if (newStr.length > maxLen) {
    break
    }

    newStr += strPart
    }

    newStr += end
return newStr
}
}