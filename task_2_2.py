import json


def text_analyze(text, maxlen, forbidden_words):
    length = len(text)  # длина текста
    pure_length = len(text.replace(' ', ''))  # Убираем пробелы

    pure_text = text
    for e in forbidden_words:
        index = pure_text.find(e)
        if index != -1:
            pure_text = pure_text.replace(e, '***')

    if maxlen < length:
        pure_short_text = pure_text[:maxlen]
        if not pure_short_text.endswith("***"):
            pure_short_text += '...'
        else:
            pure_short_text = pure_text
    else:
        pure_short_text = pure_text

    result = {
        "length": length,
        "pure_length": pure_length,
        "origin_text": text,
        "pure_text": pure_text,
        "pure_short_text": pure_short_text
    }

    print(result)
    return json.dumps(result, ensure_ascii=False, indent=4)


text = '''«Не забывайте о том, что все великие волшебники в истории в свое время были такими же, как мы, – школьниками. 
Если у них получилось, то получится и у нас», – Гарри Поттер.'''
maxlen = 35
forbidden_words = ["волшебники", "Гарри Поттер"]


text_analyze(text, maxlen, forbidden_words)